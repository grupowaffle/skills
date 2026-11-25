#!/usr/bin/env python3
"""checar_edicao.py: checagens mecânicas em uma edição antes do envio.

Uso:
    python checar_edicao.py edicao.html
    python checar_edicao.py edicao.txt

Mede o tamanho, lista os links e procura marcações esquecidas.
Saída: BLOQUEIO (não enviar), AVISO (revisar) e a lista de links.
Exit 1 se houver BLOQUEIO. Heurístico: não substitui a leitura.
"""
import re
import sys
from html import unescape
from pathlib import Path

LIMITE_GMAIL = 102_400      # bytes de HTML a partir dos quais o Gmail corta o e-mail
MARGEM_AVISO = 92_000       # a partir daqui a folga é pequena
ACRESCIMO_POR_LINK = 560    # bytes que o endereço de rastreio soma a cada link no envio
ACRESCIMO_FIXO = 1_500      # rodapé e cabeçalhos que entram no envio

MARCACOES = [
    (re.compile(r"\{\{.*?\}\}", re.S), "variável {{ ... }}"),
    (re.compile(r"\{%.*?%\}", re.S), "comando {% ... %}"),
    (re.compile(r"\*\|.*?\|\*"), "marcação *|...|*"),
    (re.compile(r"%%[A-Za-z_]+%%"), "marcação %%...%%"),
    (re.compile(r"\[(?:confirmar|nome|link|inserir|xx+|tbd)[^\]]{0,40}\]", re.I), "marcador entre colchetes"),
    (re.compile(r"\b(?:lorem ipsum|t[ií]tulo aqui|texto aqui|descri[çc][ãa]o aqui)\b", re.I), "texto de preenchimento"),
    # só em maiúsculas: "todo" é palavra comum em português
    (re.compile(r"\b(?:TODO|FIXME|XXX+)\b"), "anotação esquecida"),
]
LINK_SUSPEITO = [
    (re.compile(r"^\s*(#|javascript:)?\s*$", re.I), "link vazio"),
    (re.compile(r"^http://", re.I), "http sem s"),
    (re.compile(r"localhost|127\.0\.0\.1|\.local(?:[:/]|$)|(?://|[.-])(?:staging|preview|homolog)[.-]|/preview/|[?&]preview=", re.I), "endereço de teste ou prévia"),
    (re.compile(r"docs\.google\.com|drive\.google\.com|canva\.com/design|figma\.com|notion\.so|/edit(\?|$|#)", re.I), "endereço de rascunho ou de edição"),
    (re.compile(r"^https?://(bit\.ly|tinyurl\.com|t\.co|goo\.gl|ow\.ly|is\.gd)/", re.I), "link encurtado"),
]
ARTIGO = re.compile(r"\b(a|da|na|à|pela)\s+the\s+news\b", re.I)
MEIA_RISCA = re.compile("–")
VAZIO = re.compile(r"<(h[1-6]|p|a|li)\b[^>]*>\s*(?:&nbsp;|<br\s*/?>|\s)*</\1>", re.I)
IMG = re.compile(r"<img\b[^>]*>", re.I)
ALT = re.compile(r"\balt\s*=\s*([\"'])(.*?)\1", re.I | re.S)
A_TAG = re.compile(r"<a\b[^>]*?href\s*=\s*([\"'])(.*?)\1[^>]*>(.*?)</a>", re.I | re.S)
URL_SOLTA = re.compile(r"https?://[^\s<>\"')\]]+")
TAG = re.compile(r"<[^>]+>")


def trecho(texto, pos, raio=40):
    ini, fim = max(0, pos - raio), min(len(texto), pos + raio)
    return re.sub(r"\s+", " ", texto[ini:fim]).strip()


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    caminho = Path(sys.argv[1])
    bruto = caminho.read_bytes()
    texto = bruto.decode("utf-8", errors="replace")
    eh_html = bool(re.search(r"<(html|body|table|div|p|a)\b", texto, re.I))
    bloqueios, avisos = [], []

    # links
    links = []
    if eh_html:
        for m in A_TAG.finditer(texto):
            ancora = re.sub(r"\s+", " ", unescape(TAG.sub("", m.group(3)))).strip()
            links.append((unescape(m.group(2)).strip(), ancora or "(sem texto: imagem ou vazio)"))
    else:
        links = [(u.rstrip(".,;"), "") for u in URL_SOLTA.findall(texto)]
    for url, ancora in links:
        for rx, motivo in LINK_SUSPEITO:
            if rx.search(url):
                bloqueios.append(f"link suspeito ({motivo}): {url or '(vazio)'}  [{ancora}]")
                break
    vistos = {}
    for url, _ in links:
        vistos[url] = vistos.get(url, 0) + 1
    for url, n in vistos.items():
        if n > 2 and url:
            avisos.append(f"link repetido {n} vezes: {url}")

    # marcações esquecidas (no texto visível e nos endereços)
    for rx, nome in MARCACOES:
        for m in rx.finditer(texto):
            bloqueios.append(f"{nome}: \"{trecho(texto, m.start())}\"")

    # texto e estrutura
    visivel = unescape(TAG.sub(" ", texto)) if eh_html else texto
    for m in ARTIGO.finditer(visivel):
        avisos.append(f"artigo feminino: \"{trecho(visivel, m.start())}\" (é o/do/no the news)")
    if MEIA_RISCA.search(visivel):
        avisos.append(f"meia-risca (–) em {len(MEIA_RISCA.findall(visivel))} ponto(s): use travessão (—)")
    if eh_html:
        for m in VAZIO.finditer(texto):
            depois = re.sub(r"\s+", " ", unescape(TAG.sub(" ", texto[m.end():m.end() + 300]))).strip()[:60]
            bloqueios.append(f"bloco <{m.group(1).lower()}> vazio, antes de: \"{depois}\"")
        for m in IMG.finditer(texto):
            alt = ALT.search(m.group(0))
            largura_1px = re.search(r"\b(width|height)\s*=\s*[\"']?1[\"'\s>]", m.group(0), re.I)
            if (not alt or not alt.group(2).strip()) and not largura_1px:
                src = re.search(r"\bsrc\s*=\s*[\"'](.*?)[\"']", m.group(0), re.I)
                avisos.append(f"imagem sem texto alternativo: {(src.group(1) if src else '?')[-70:]}")

    # tamanho
    tamanho = len(bruto)
    if eh_html:
        estimado = tamanho + ACRESCIMO_POR_LINK * len(links) + ACRESCIMO_FIXO
        linha = (f"tamanho: {tamanho/1000:.1f} KB no arquivo, cerca de {estimado/1000:.1f} KB no envio "
                 f"({len(links)} links). limite do Gmail: {LIMITE_GMAIL/1000:.0f} KB")
        if estimado > LIMITE_GMAIL:
            bloqueios.append(linha + ". vai cortar: enxugue antes de agendar")
        elif estimado > MARGEM_AVISO:
            avisos.append(linha + ". folga pequena")
        else:
            print(linha + ". ok")
        print("  (estimativa vale para o HTML completo do e-mail; se o arquivo é só o miolo, confira o alerta de corte no HuB)")
    else:
        print("tamanho: não medido. o arquivo é texto, não HTML; confira o alerta de corte no HuB.")

    print(f"\n{len(links)} link(s):")
    for i, (url, ancora) in enumerate(links, 1):
        print(f"  {i:>2}. {ancora[:50]:<50} {url}")
    print()
    for b in bloqueios:
        print(f"BLOQUEIO  {b}")
    for a in avisos:
        print(f"AVISO     {a}")
    print(f"\n{len(bloqueios)} bloqueio(s), {len(avisos)} aviso(s). os links foram listados, não abertos: clique em cada um.")
    sys.exit(1 if bloqueios else 0)


if __name__ == "__main__":
    main()
