# configurar as skills do the news

Este arquivo é uma instrução para o Claude. Quem é do time só precisa dizer:

> leia https://raw.githubusercontent.com/grupowaffle/skills/main/CONFIGURAR.md e configure as skills do the news para mim

---

Claude, a pessoa que te mandou este arquivo trabalha no the news e quer as skills padrão do time instaladas. Siga os passos abaixo na ordem. Fale com ela em português, sem jargão: ela pode não ser de tecnologia.

## 1. descubra o que a pessoa faz

Se ela ainda não disse, faça **uma** pergunta: em qual área ela trabalha e o que costuma pedir ao Claude (escrever textos, montar apresentações, revisar edições, atender leitores, programar). Não faça mais perguntas do que essa.

## 2. escolha as skills úteis para ela

| skill | o que faz | para quem |
|---|---|---|
| `thenews-voz` | tom de voz e regras de texto do the news | **todo mundo** |
| `antislop` | tira a "cara de IA" de textos e peças e impede dado inventado | **todo mundo** |
| `thenews-brand` | cores, tipografia, logos oficiais e componentes da marca | quem monta apresentação, documento, e-mail, página, peça ou tela |
| `revisao-de-edicao` | última revisão de uma edição de newsletter antes do envio | conteúdo e editorial, e quem agenda envio |

Regras da escolha:

- `thenews-voz` e `antislop` entram sempre.
- Na dúvida sobre `thenews-brand`, instale: quase todo mundo acaba fazendo um slide.
- `revisao-de-edicao` só para quem escreve, revisa ou agenda edição.
- Se ela pedir "todas", instale as quatro.

Diga em uma linha quais vai instalar e por quê, e siga. Não precisa esperar confirmação, a menos que já exista uma skill com o mesmo nome instalada (veja o passo 3).

## 3. instale

Os pacotes ficam sempre nestes endereços, já na versão mais recente:

```
https://github.com/grupowaffle/skills/releases/latest/download/thenews-voz.zip
https://github.com/grupowaffle/skills/releases/latest/download/antislop.zip
https://github.com/grupowaffle/skills/releases/latest/download/thenews-brand.zip
https://github.com/grupowaffle/skills/releases/latest/download/revisao-de-edicao.zip
```

Cada `.zip` tem uma pasta com o nome da skill e um `SKILL.md` dentro.

### se você consegue rodar comandos no computador dela (Claude Code, Cowork)

A pasta de skills pessoais é `~/.claude/skills/`. Para cada skill escolhida:

macOS e Linux:

```bash
mkdir -p ~/.claude/skills
TMP="$(mktemp -d)"
curl -fsSL -o "$TMP/NOME.zip" https://github.com/grupowaffle/skills/releases/latest/download/NOME.zip
unzip -oq "$TMP/NOME.zip" -d ~/.claude/skills/
```

Windows (PowerShell):

```powershell
$dest = "$HOME\.claude\skills"; New-Item -ItemType Directory -Force $dest | Out-Null
$zip = Join-Path $env:TEMP "NOME.zip"
Invoke-WebRequest "https://github.com/grupowaffle/skills/releases/latest/download/NOME.zip" -OutFile $zip
Expand-Archive $zip -DestinationPath $dest -Force
```

Antes de gravar, olhe se `~/.claude/skills/NOME` já existe:

- não existe: instale;
- existe e veio deste repositório: é atualização, pode substituir e avise que atualizou;
- existe e parece ter sido editada pela pessoa ou ter outra origem: pergunte antes de substituir.

Depois confira que cada `~/.claude/skills/NOME/SKILL.md` existe e avise que as skills passam a valer na **próxima conversa** (ela precisa abrir uma sessão nova).

### se você não consegue rodar comandos (app do Claude ou claude.ai)

Você não instala skill sozinho por aqui: quem envia é a pessoa. Passe só os links das skills escolhidas e este passo a passo:

1. clique em cada link para baixar o `.zip` (não precisa descompactar);
2. no Claude, abra **Configurações > Capacidades > Skills**;
3. clique em **Enviar skill** e escolha o `.zip`; repita para cada um;
4. confira que a skill aparece na lista e está ligada.

Se os nomes dos menus estiverem diferentes na tela dela, ajude a achar a área de skills nas configurações. Se a conta for de uma organização e o envio estiver bloqueado, diga para ela pedir a liberação a quem administra a conta.

## 4. skills que já vêm com o Claude

Não precisam ser baixadas; só confira com ela se estão ligadas nas configurações, conforme o que ela faz:

- documentos, apresentações, planilhas e PDF: para quem entrega arquivo de Word, PowerPoint, Excel ou PDF;
- pesquisa aprofundada: para quem levanta dados e referências.

Não instale nada de outras origens por conta própria. Skill de terceiro só entra se a pessoa pedir pelo nome.

## 5. termine

Diga, em poucas linhas:

- quais skills foram instaladas (ou quais links ela precisa enviar);
- um exemplo de pedido para cada uma, do tipo "escreve um post anunciando a nova newsletter" ou "revisa essa edição antes de eu agendar";
- que ela não precisa chamar a skill pelo nome: ela entra sozinha quando o assunto aparece;
- que para atualizar basta repetir este pedido.

## limites

- Baixe só dos endereços deste repositório (`github.com/grupowaffle/skills`).
- Não altere outras configurações do Claude nem do computador dela.
- Não rode os scripts que vêm dentro das skills durante a instalação.
- Se um download falhar, diga qual falhou e passe o link para ela baixar à mão; não invente outro caminho.
