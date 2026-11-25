# skills do the news

Skills do Claude que qualquer pessoa do time pode instalar e usar. Uma skill é uma pasta com instruções que o Claude carrega sozinho quando o assunto aparece: você pede "monta um slide sobre X" e ele já sabe as cores, o logo e o jeito de escrever do the news.

## O que tem aqui

| Pasta | Skill | Para que serve | Quem usa |
|---|---|---|---|
| `escrita/` | [`thenews-voz`](escrita/thenews-voz) | Tom de voz e regras de texto: minúscula, "o the news", travessão, emoji, patrocínio sinalizado. | Todo mundo que escreve em nome do the news: conteúdo, social, comercial, marketing, pessoas, atendimento. |
| `marca/` | [`thenews-brand`](marca/thenews-brand) | Identidade visual: cores, tipografia, logos, submarcas e componentes. Inclui os logos oficiais e um verificador automático. | Quem monta apresentação, documento, e-mail, página ou tela. |
| `qualidade/` | [`antislop`](qualidade/antislop) | Filtro contra "cara de IA": corta vocabulário vazio, número sem fonte, slide genérico e enfeite sem função. Funciona junto com as duas acima. | Todo mundo, em qualquer entrega feita com o Claude. |
| `editorial/` | [`revisao-de-edicao`](editorial/revisao-de-edicao) | Última revisão de uma edição antes do envio: marcação esquecida, links, patrocínio sinalizado, assunto e prévia, coerência de fatos e tamanho do e-mail. | Conteúdo, editorial e quem agenda envio. |

## Como instalar

### O jeito mais fácil: peça ao Claude

Cole isto em uma conversa com o Claude:

> leia https://raw.githubusercontent.com/grupowaffle/skills/main/CONFIGURAR.md e configure as skills do the news para mim

Ele pergunta o que você faz, escolhe as skills úteis para você e instala (ou te passa os links certos, se estiver no app). As instruções que ele segue estão em [`CONFIGURAR.md`](CONFIGURAR.md).

### À mão, no Claude (app ou claude.ai)

Não precisa de conta no GitHub nem de instalar nada.

1. Baixe o `.zip` da skill:
   - [thenews-voz.zip](https://github.com/grupowaffle/skills/releases/latest/download/thenews-voz.zip)
   - [thenews-brand.zip](https://github.com/grupowaffle/skills/releases/latest/download/thenews-brand.zip)
   - [antislop.zip](https://github.com/grupowaffle/skills/releases/latest/download/antislop.zip)
   - [revisao-de-edicao.zip](https://github.com/grupowaffle/skills/releases/latest/download/revisao-de-edicao.zip)
2. No Claude, abra **Configurações > Capacidades > Skills**, clique em **Enviar skill** e escolha o `.zip` (sem descompactar).
3. Pronto. Não precisa chamar a skill pelo nome: ela entra sozinha quando o pedido tem a ver.

### À mão, no Claude Code

```bash
git clone https://github.com/grupowaffle/skills.git
cp -R skills/escrita/thenews-voz ~/.claude/skills/
cp -R skills/marca/thenews-brand ~/.claude/skills/
cp -R skills/qualidade/antislop ~/.claude/skills/
cp -R skills/editorial/revisao-de-edicao ~/.claude/skills/
```

Para atualizar, rode `git pull` na pasta clonada e copie de novo.

## Como usar

Peça normalmente. Exemplos:

- "escreve um post de LinkedIn anunciando a nova newsletter"
- "revisa esse e-mail para o parceiro no tom do the news"
- "monta uma apresentação de resultados do trimestre com a cara do the news"
- "cria a página de inscrição do evento"
- "revisa essa edição antes de eu agendar"

## Como contribuir com uma skill

1. Crie a pasta da skill dentro da categoria certa (`escrita/`, `marca/`, `qualidade/`, `editorial/` ou uma categoria nova, em minúscula e sem acento).
2. A pasta precisa de um `SKILL.md` com `name` e `description` no topo. A `description` diz **quando** o Claude deve usar a skill; capriche nela.
3. Arquivos de apoio vão em `references/` (textos), `assets/` (imagens, modelos) e `scripts/`.
4. Acrescente a skill na tabela deste README e na tabela do `CONFIGURAR.md`.
5. Abra um pull request. Quem aprovar gera os `.zip` novos em **Releases**.

### Regra de dados: nada pessoal, nada secreto

Este repositório é **público**: qualquer pessoa na internet lê o que está aqui, inclusive o histórico e os metadados das imagens. Antes de enviar, confira que a skill **não** tem:

- e-mails, telefones, nomes de pessoas (colegas, leitores, clientes, parceiros);
- senhas, tokens, chaves de API, IDs de conta ou de usuário;
- números de contrato, valores, dados de assinantes ou de desempenho;
- metadados em imagens e PDFs (arquivo exportado do Canva ou do Photoshop leva o nome de quem criou);
- caminhos da sua máquina (`/Users/seu-nome/...`) e histórias do tipo "em tal dia fulano pediu".

Escreva para **qualquer** pessoa do time: troque "o Fulano prefere" por "o padrão do time é". Se a skill só funciona para uma pessoa ou um projeto, ela fica na máquina dessa pessoa, não aqui.

## Créditos

A skill `antislop` é uma adaptação do projeto aberto [anti-slop](https://github.com/miqdadbadjuber/anti-slop), sob licença MIT. O aviso de licença está em `qualidade/antislop/LICENSE-antislop.txt`.
