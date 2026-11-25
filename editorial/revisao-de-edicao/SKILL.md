---
name: revisao-de-edicao
description: Revisão de uma edição de newsletter do the news antes do envio. Use SEMPRE que alguém colar, anexar ou apontar uma edição (texto, HTML ou link de prévia) e pedir para revisar, conferir, checar, "dar uma olhada antes de mandar", "ver se está tudo certo" ou "posso agendar?", para qualquer caderno (the news, morning, night, money, sports, trends, business, health, around, cult, elections, travel, better work, rising). Também use para conferir assunto e prévia de e-mail, links, sinalização de patrocínio e tamanho do e-mail.
---

# revisão de edição antes do envio

Depois que a edição sai, não tem como corrigir: o erro chega em centenas de milhares de caixas de entrada. Esta skill é a última leitura antes de agendar. O papel aqui é de **revisor**: apontar o que impede o envio e o que melhora, sem reescrever a edição nem mudar a voz de quem escreveu.

Trabalha junto com `thenews-voz` (estilo) e `antislop` (fato inventado e cara de IA). Se elas estiverem instaladas, valem as regras delas.

## o que pedir antes de começar

Se não estiver no pedido, pergunte de uma vez só:

1. qual caderno e qual a data e hora de envio;
2. o assunto e o texto de prévia (os dois, se houver teste A/B);
3. se há patrocinador na edição e em quais blocos.

Sem a edição completa não há revisão: diga o que falta. Revisar só um trecho é permitido, desde que o relatório diga que o resto não foi visto.

## como revisar

1. Se a edição veio em HTML ou arquivo e houver como rodar código, rode `python scripts/checar_edicao.py <arquivo>`. Ele mede o tamanho, lista os links e acha marcações esquecidas. Sem código, faça as mesmas checagens lendo.
2. Leia a edição inteira uma vez, do assunto ao rodapé, como leitor.
3. Passe os sete blocos abaixo, na ordem.
4. Entregue o relatório no formato do fim deste arquivo.

## 1. o que impede o envio

Qualquer item aqui é **bloqueio**: a edição não deve sair até ser resolvido.

- **Marcação esquecida no texto**: `{{ ... }}`, `{% ... %}`, `*|...|*`, `%%...%%`, `[NOME]`, `[confirmar]`, `XXX`, `TODO`, "lorem ipsum", "título aqui". Código de personalização colado de outra ferramenta pode fazer o envio inteiro falhar. Só ficam as variáveis que o próprio editor do HuB insere; na dúvida, aponte.
- **Bloco vazio ou quebrado**: título sem texto, seção só com o cabeçalho, imagem que não carrega, botão sem link, parágrafo cortado no meio.
- **Link errado**: vazio, `#`, `http://` sem "s", endereço de rascunho ou de edição (documento compartilhado, ferramenta de design, prévia, `localhost`, ambiente de teste), link encurtado de origem desconhecida, ou texto do link que promete uma coisa e leva a outra.
- **Patrocínio sem sinalização**: todo conteúdo pago leva "powered by", "patrocinado" ou equivalente, visível e junto do bloco. Anúncio com cara de matéria é bloqueio.
- **Caderno ou data trocados**: nome de outra submarca no cabeçalho ou no texto, dia da semana que não bate com a data de envio, "hoje", "ontem" e "amanhã" incoerentes com o dia em que o leitor vai ler.
- **Fato sem origem**: número, citação, nome ou cargo que parece inventado ou que contradiz outro trecho da mesma edição.
- **Tamanho acima do limite do Gmail** (ver bloco 6).

## 2. assunto e prévia

- Começam em minúscula e seguem `thenews-voz`.
- O assunto diz algo da edição de hoje; não serve para qualquer dia.
- Curto o bastante para não cortar no celular. Acima de uns 50 caracteres, avise.
- A prévia completa o assunto, não repete.
- Em teste A/B, os dois assuntos são diferentes de verdade e os dois estão revisados.
- Sem CAIXA ALTA de grito, sem "RE:" ou "urgente" falsos, sem promessa que a edição não cumpre.

## 3. links

Para cada link: o destino existe, é o certo e é a versão pública.

- Com ferramenta de navegação, abra cada um. Sem ela, **não diga que os links funcionam**: liste todos com o texto âncora e peça para a pessoa clicar na prévia.
- Link de fonte aponta para a matéria ou o documento, não para a página inicial do site.
- Link de patrocinador é exatamente o que o cliente mandou, com os parâmetros de rastreio dele intactos.
- Nenhum link repetido por engano em blocos diferentes.
- O rodapé e os links de descadastro são gerados pelo sistema: não mexa e não sugira mudança neles.

## 4. fatos e números

A revisão não substitui a checagem do jornalista, mas pega incoerência.

- Número bate com o próprio texto: soma, porcentagem, ordem de grandeza (milhão e bilhão), moeda, unidade.
- Nome próprio escrito igual em toda a edição; cargo e empresa coerentes.
- Citação tem autor. "especialistas dizem" sem nome é para apontar.
- Título e texto dizem a mesma coisa. Título que promete mais do que o texto entrega é para apontar.
- Datas e prazos fazem sentido para quem lê no dia do envio.
- O que não dá para verificar daqui entra no relatório como **conferir**, dizendo exatamente o quê e onde. Nunca "corrija" um fato por conta própria.

## 5. texto e voz

- Padrão `thenews-voz`: minúscula no início de títulos, "o the news", travessão (—) e nunca meia-risca, emoji só na ponta da frase.
- Ortografia, concordância, palavra repetida, frase duplicada, espaço duplo, pontuação dobrada.
- Imparcialidade: sem adjetivo opinativo sobre governo, partido ou candidato; os dois lados quando o assunto tem dois lados.
- Sinais de texto de IA (`antislop`): abertura de "no mundo de hoje", vocabulário vazio, fecho otimista.
- Sugestão de estilo é **sugestão**. Não troque a piada, o tom ou a escolha de palavra de quem escreveu por gosto.

## 6. tamanho

O Gmail corta o e-mail que passa de **102 KB** de código (o HTML; imagem não conta). O leitor vê "mensagem cortada", perde o fim da edição, e a abertura deixa de ser contada.

- O que pesa: quantidade de texto, de blocos e, principalmente, de **links**. Cada link ganha um endereço de rastreio longo no envio, então a edição entregue é maior do que a que se vê no editor.
- Se o HuB mostrar o alerta de corte, é bloqueio: enxugue antes de agendar.
- Com o HTML em mãos, o script estima o tamanho entregue. Acima de 102 KB é bloqueio; acima de 92 KB é aviso, porque a margem é pequena.
- Só com o texto colado não dá para medir: diga isso no relatório e peça para conferir o alerta no HuB.
- Para emagrecer: cortar um bloco inteiro rende mais do que aparar frases; tirar links repetidos; encurtar listas longas de links.

## 7. imagens

- Toda imagem tem texto alternativo que descreve o que ela mostra.
- Crédito ou fonte quando a imagem não é do the news.
- Imagem de patrocinador é a que o cliente aprovou.
- Texto importante não fica só dentro da imagem: quem lê com imagens bloqueadas precisa entender a edição.
- Logo é o arquivo oficial (`thenews-brand`), nunca recriado.

## formato do relatório

Curto, na ordem do que a pessoa precisa decidir. Sempre com o trecho citado e onde ele está.

```
veredito: pode agendar | pode agendar depois dos ajustes | não agendar

bloqueios (resolver antes de enviar)
1. [bloco ou seção] "trecho exato" → o problema → a correção sugerida

ajustes (melhoram, não impedem)
1. [bloco] "trecho" → sugestão

conferir (não deu para verificar daqui)
1. [bloco] o que conferir e como

o que foi checado
caderno, data, assunto e prévia, N links, tamanho (medido, estimado ou não medido), patrocínio
```

Regras do relatório:

- "não agendar" sempre que houver um bloqueio.
- Nada de elogio de enchimento nem resumo da edição: a pessoa escreveu, ela sabe o que tem.
- Se não achou nada, diga isso em uma linha e liste o que foi checado e o que não foi.
- Nunca afirme que algo está certo sem ter verificado. "não verifiquei" é resposta válida.
- Não devolva a edição reescrita, a menos que peçam.
