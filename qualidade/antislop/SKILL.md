---
name: antislop
description: Filtro de qualidade do the news contra "cara de IA" em qualquer entrega. Use SEMPRE que for escrever, revisar ou montar algo que outra pessoa vai ler ou ver, como post, legenda, e-mail, comunicado, proposta, mídia kit, relatório, roteiro, apresentação, slide, documento, página, landing page ou peça visual, mesmo que o pedido não fale em "IA", "slop" ou "revisão". Também use quando pedirem para "deixar mais humano", "tirar a cara de ChatGPT", "revisar o texto" ou "melhorar o layout", e antes de entregar qualquer conteúdo com número, depoimento, citação ou dado.
---

# antislop: filtro de qualidade do the news

"Slop" é o resultado genérico que a IA entrega quando ninguém decide nada: texto que serve para qualquer empresa, slide igual a todos os outros, número que ninguém sabe de onde veio. Esta skill diz **o que cortar**. O que colocar no lugar vem das skills `thenews-voz` (texto) e `thenews-brand` (visual). Se houver conflito entre esta skill e as duas, a marca vence.

Adaptada do projeto aberto [anti-slop](https://github.com/miqdadbadjuber/anti-slop), de Miqdad Badjuber (licença MIT, em `LICENSE-antislop.txt`), para português, para o padrão do the news e para quem não programa.

## O teste que decide tudo

Antes de manter qualquer frase, bloco, cor, ícone ou efeito, responda: **isso serve a quê?**

- Se a resposta nomeia algo real (informa, organiza, destaca o que importa, é da marca), fica.
- Se a resposta é "fica bonito", "parece profissional" ou "todo mundo faz assim", sai.

E antes de entregar:

> Se eu trocar "the news" pelo nome de outra empresa, a peça continua servindo igualzinho?

Se sim, está genérica. Refaça com o que só o the news diria, mostraria ou saberia.

## Três regras que não têm exceção

1. **Nunca invente fato.** Nenhum número, nome, data, citação, depoimento, cliente, prêmio ou resultado que não esteja no material recebido ou que a pessoa não tenha confirmado. Somos uma empresa de notícia: dado inventado é o pior erro possível. Faltou o dado? Pergunte, ou escreva a versão simples sem ele, ou deixe um marcador visível como `[número de assinantes: confirmar]`. Marcador nunca vai para a versão final.
2. **Afirmação precisa de prova ou de corte.** "líder", "o maior", "referência", "milhares de leitores", "especialistas dizem" só ficam com a fonte ao lado. Sem fonte, corte a frase.
3. **Patrocínio sempre sinalizado e nenhum lado político.** Regras da marca, repetidas aqui porque a IA esquece.

## Como usar

1. Leia o pedido e o material. Liste para você mesmo o que é fato confirmado.
2. Produza seguindo `thenews-voz` e `thenews-brand`.
3. Passe o filtro certo:
   - texto de qualquer tipo: `references/texto.md`
   - slide, documento, página ou peça visual: `references/visual.md`
4. Rode a auditoria abaixo e corrija.
5. Entregue. Se cortou alguma afirmação por falta de fonte, avise a pessoa em uma linha, dizendo o que falta para ela voltar.

## Um sinal sozinho não é problema

Os padrões das referências são um **diagnóstico**, não uma lista de proibições. Um travessão, uma lista de três ou uma frase curta não condenam nada. O problema é o acúmulo: vários sinais juntos, sem motivo. Procure o conjunto.

E não esterilize. Texto sem voz e slide sem identidade são tão "de máquina" quanto os cheios de vícios. Tirar o slop é metade do trabalho; a outra metade é a peça ter a cara do the news: direta, próxima, irônica na medida, com um único destaque amarelo.

Texto que a pessoa escreveu e não pediu para mudar fica como está. Se ela mandou um trecho no estilo dela, siga o estilo dela.

## Auditoria antes de entregar

Faça as três perguntas e responda com honestidade:

1. **O que aqui entrega que foi feito por IA?** Corrija o que aparecer.
2. **Tem algum fato, número, nome, data ou citação que não veio do material?** Se tem, corte ou marque para confirmar.
3. **Dá para cortar?** Corte. "10 linhas o que outros dizem em 50."

## Checklist final

- [ ] Nenhum fato, número, depoimento ou nome inventado. Marcadores `[confirmar]` resolvidos ou apontados para a pessoa.
- [ ] Toda afirmação de grandeza tem fonte ou foi cortada.
- [ ] Sem vocabulário vazio, sem abertura de "no mundo de hoje", sem fecho otimista genérico (`references/texto.md`).
- [ ] Cada frase diz quem fez o quê.
- [ ] Texto no padrão `thenews-voz`: minúscula, "o the news", emoji na ponta.
- [ ] Visual no padrão `thenews-brand`: só cores da marca, plano, sem efeito decorativo (`references/visual.md`).
- [ ] Um ponto focal por tela ou slide. Um destaque amarelo, não dez.
- [ ] Trocando o nome da empresa, a peça **não** serve para outra.
- [ ] Lido em voz alta, parece uma pessoa falando.
