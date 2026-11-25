#!/usr/bin/env python3
"""check_brand.py — verifica violações do brand guidelines do the news em arquivos de UI.

Uso:
    python check_brand.py src/            # pasta (recursivo)
    python check_brand.py a.tsx b.css     # arquivos

Saída: lista de ERRO (viola regra inegociável) e AVISO (revisar). Exit 1 se houver ERRO.
Heurístico: não substitui revisão, mas pega os deslizes mais comuns.
"""
import re
import sys
from pathlib import Path

EXTS = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".jsx", ".tsx", ".js", ".ts",
        ".vue", ".svelte", ".astro", ".mdx", ".md", ".json", ".liquid", ".hbs", ".ejs", ".mjml"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "coverage", "vendor", ".turbo"}
SKIP_FILES = {"tokens.css", "tailwind.preset.js", "tokens.json", "package-lock.json", "yarn.lock", "pnpm-lock.yaml"}

ALLOWED_HEX = {
    # marca
    "ffcd00", "ff8e42", "000000", "ffffff", "fff", "000",
    # semânticos (tokens.css)
    "f2f2f2", "555555", "1a1a1a", "bdbdbd", "e0e0e0", "333333", "f70301", "00bf63",
    # submarcas
    "374b84", "2aa0a7", "f97f2e", "3632ca", "f742a1", "760102", "94eeff", "6a98ff",
    "4f5025", "d9c8ba", "dc4659", "f4b0b2", "1906ae", "6c9bf7", "9a9a9a",
}
ALLOWED_FONTS = re.compile(r"helvetica now display|inter tight|helvetica|arial|sans-serif|var\(|inherit|"
                           r"ui-monospace|sfmono|menlo|monospace|consolas|system-ui|-apple-system", re.I)

TW_DEFAULT_COLORS = ("slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|"
                     "cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose")
RX = {
    "hex": re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b"),
    "tw_color": re.compile(rf"\b(?:bg|text|border|ring|fill|stroke|from|to|via|outline|decoration|divide|shadow)-(?:{TW_DEFAULT_COLORS})-\d{{2,3}}\b"),
    "artigo": re.compile(r"\b(a|da|na|à|pela)\s+the\s+news\b", re.I),
    "meia_risca": re.compile(r"\u2013"),
    "font_family": re.compile(r"font-?family\s*:\s*['\"`]?([^;}\n'\"`]+)", re.I),
    "font_import": re.compile(r"fonts\.googleapis\.com/css2?\?family=([A-Za-z+]+)"),
    "amarelo_texto": re.compile(r"(?<![\w-])color\s*:\s*['\"`]?(#ffcd00|#ff8e42|var\(--tn-amarelo\)|var\(--tn-laranja\)|var\(--highlight\))", re.I),
    "tw_amarelo_texto": re.compile(r"\btext-(amarelo|laranja)\b"),
    "laranja_solido": re.compile(r"(?:background(?:-color|Color)?\s*:\s*['\"`]?(?:#ff8e42|var\(--tn-laranja\))['\"`]?\s*[;,}])|\bbg-laranja\b", re.I),
    "shadow": re.compile(r"box-shadow\s*:\s*(?!none|inset\s+0\s+0\s+0)[^;]+;", re.I),
    "tw_shadow": re.compile(r"\bshadow-(sm|md|lg|xl|2xl)\b|\bshadow\b(?!-)"),
    "radius": re.compile(r"border-radius\s*:\s*([^;]+);", re.I),
    "tw_radius": re.compile(r"\brounded-(sm|md|lg|xl|2xl|3xl)\b|\brounded\b(?!-)"),
    "logo_texto": re.compile(r"class(?:Name)?=[\"'][^\"']*logo[^\"']*[\"'][^>]*>\s*the\s*news\s*<", re.I),
    "capitalizado": re.compile(r"<(button|h[1-4]|label|a|th)\b[^>]*>\s*([A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]{2,}(?:\s+[A-Za-záéíóúâêôãõçÁÉÍÓÚÂÊÔÃÕÇ]+)+)"),
    "emoji_meio": re.compile(r"[A-Za-zÀ-ÿ,]\s+[\U0001F300-\U0001FAFF\u2600-\u27BF]\s+[a-zà-ÿ]"),
}
RADIUS_OK = re.compile(r"^\s*(0|0px|16px|1rem|50%|9999px|var\(--radius-[\w-]+\))\s*$", re.I)


def files_from(args):
    for a in args:
        p = Path(a)
        if p.is_dir():
            for f in p.rglob("*"):
                if f.is_file() and f.suffix in EXTS and not (set(f.parts) & SKIP_DIRS) and f.name not in SKIP_FILES:
                    yield f
        elif p.is_file():
            yield p


def check(path):
    out = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return [("AVISO", 0, f"não consegui ler: {e}")]
    for n, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        for m in RX["hex"].finditer(line):
            if m.group(1).lower() not in ALLOWED_HEX:
                out.append(("ERRO", n, f"cor fora da paleta: #{m.group(1)} — use uma variável de tokens.css"))
        for m in RX["tw_color"].finditer(line):
            out.append(("ERRO", n, f"cor padrão do Tailwind '{m.group(0)}' — use o preset da marca"))
        for m in RX["artigo"].finditer(line):
            out.append(("ERRO", n, f"'{m.group(0)}' — artigo é masculino: o/do/no the news"))
        if RX["meia_risca"].search(line):
            out.append(("ERRO", n, "meia-risca (–) — use travessão (—)"))
        for m in RX["font_family"].finditer(line):
            fams = [f.strip().strip("'\"") for f in m.group(1).split(",")]
            bad = [f for f in fams if f and not ALLOWED_FONTS.search(f)]
            if bad:
                out.append(("ERRO", n, f"fonte fora da marca: {', '.join(bad)}"))
        for m in RX["font_import"].finditer(line):
            if "inter+tight" not in m.group(1).lower():
                out.append(("ERRO", n, f"import de fonte fora da marca: {m.group(1)}"))
        if RX["amarelo_texto"].search(line) or RX["tw_amarelo_texto"].search(line):
            out.append(("AVISO", n, "amarelo/laranja como cor de texto — só permitido sobre fundo preto"))
        if RX["laranja_solido"].search(line):
            out.append(("ERRO", n, "laranja sólido — laranja só existe dentro do degradê"))
        if RX["shadow"].search(line) or RX["tw_shadow"].search(line):
            out.append(("AVISO", n, "sombra — a marca é plana; hierarquia por cor, peso e espaço"))
        for m in RX["radius"].finditer(line):
            if not RADIUS_OK.match(m.group(1)):
                out.append(("AVISO", n, f"border-radius {m.group(1).strip()} — use 0, 16px ou 50%"))
        if RX["tw_radius"].search(line):
            out.append(("AVISO", n, "rounded-* do Tailwind — use rounded-none, rounded-pill ou rounded-full"))
        if RX["logo_texto"].search(line):
            out.append(("ERRO", n, "logo escrito como texto — use os PNGs originais de assets/logos"))
        for m in RX["capitalizado"].finditer(line):
            out.append(("AVISO", n, f"texto de UI começando em maiúscula: '{m.group(2)[:40]}' — use minúscula (exceto nome próprio)"))
        if RX["emoji_meio"].search(line):
            out.append(("AVISO", n, "emoji no meio da frase — só no início ou no fim"))
        if ("laranja" in low or "ff8e42" in low) and "gradient" in low and re.search(r"90deg[^)]*ffcd00[^)]*ff8e42|90deg[^)]*amarelo[^)]*laranja", low):
            out.append(("AVISO", n, "degradê invertido? horizontal é laranja → amarelo (esquerda → direita)"))
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total_err = total_warn = 0
    for f in files_from(sys.argv[1:]):
        issues = check(f)
        for lvl, n, msg in issues:
            print(f"{lvl:5} {f}:{n}  {msg}")
        total_err += sum(1 for i in issues if i[0] == "ERRO")
        total_warn += sum(1 for i in issues if i[0] == "AVISO")
    print(f"\n{total_err} erro(s), {total_warn} aviso(s)")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
