---
name: thenews-brand
description: Brand guidelines do the news / grupo tns (thenews.com.br) para qualquer interface ou peça visual. Use SEMPRE que for criar, editar, revisar ou estilizar algo com a cara do the news ou tns — apresentações, slides, documentos, relatórios, propostas, mídia kit, páginas, componentes React/Vue/HTML, telas de app, dashboards internos, emails/newsletters, landing pages, formulários, CSS/Tailwind, temas, ícones, empty states, microcopy — mesmo que o pedido não mencione "marca", "brand" ou "design". Também use ao escolher cores, fontes, espaçamentos, raios, logos ou ao escrever textos de interface (botões, títulos, erros, onboarding) para qualquer produto do grupo (the news, morning, night, money, sports, trends, business, health, around, cult, elections, travel, better work, HuB).
---

# the news — brand guidelines para UI

Fonte: brandbook the news 2026 (tns) + design system "the news". Este arquivo é a regra; `references/` tem os detalhes.

Princípios de design da marca, que decidem qualquer dúvida não coberta aqui:
**simplicidade** (remova o que não é essencial), **clareza** (se precisa de explicação, não está pronto), **propósito** (cada detalhe tem razão de existir), **experiência** (design é como funciona, não como parece).

## Fluxo obrigatório

1. Antes de escrever UI, carregue os tokens: copie `references/tokens.css` para o projeto (ou importe) e use **só** as variáveis dele. Em Tailwind, use `references/tailwind.preset.js`.
2. Se a peça for de uma submarca, leia `references/submarcas.md`.
3. Para componentes (botão, card, pílula, eyebrow, tarja, número, tabela, nav, termômetro), siga `references/componentes.md`.
4. Para qualquer texto visível ao usuário, siga `references/voz-e-texto.md`.
5. Ao terminar, rode `python scripts/check_brand.py <arquivos ou pasta>` e corrija tudo que ele apontar.

## Regras inegociáveis

### Cor
- Marca = **amarelo `#FFCD00`, preto `#000000`, branco `#FFFFFF`**. Cinza de apoio `#F2F2F2` (surface-alt).
- **Laranja `#FF8E42` só existe dentro do degradê** laranja → amarelo (esquerda → direita). Nunca laranja sólido em botão, texto, borda ou fundo.
- **Amarelo nunca é cor de texto sobre fundo claro** (contraste ~1.4:1, reprova WCAG). Sobre branco, amarelo é fundo (pílula, highlight, barra) com texto preto.
- Amarelo como texto só sobre preto.
- Sem cores fora dos tokens. Nada de azul de link padrão, verde/vermelho genéricos de Tailwind, cinzas aleatórios. Estados de sucesso/erro usam os tokens `--feedback-*` de `tokens.css`.
- Cores de submarca só em peças daquela submarca.

### Tipografia
- Família única: **Helvetica Now Display**; fallback **Inter Tight** (Google Fonts, pesos 300/400/700/800/900). Stack: `"Helvetica Now Display", "Inter Tight", Helvetica, Arial, sans-serif`.
- Títulos, números e destaques: **Black (900) ou Bold (700)**, `letter-spacing: -0.02em` (o "-20" do brandbook).
- Texto longo, subtítulos e apoio: **Light (300)**, `letter-spacing: 0`. Abaixo de 16px use 400 para legibilidade.
- Proibido: serifadas, monoespaçada fora de código, segunda família "para variar", itálico decorativo.

### Logo
- Use **sempre os PNGs originais** de `assets/logos/`. Nunca recrie o logo em CSS/SVG/texto, nunca recolora, distorça ou anime a forma.
- `the-news-preto.png` em fundo claro; `the-news-branco.png` em fundo preto. Em fundo degradê amarelo → laranja, o logo pode ser branco ou preto.
- Assinatura institucional (header, footer, login, email) = logo completo (caneca + "the news"). Texto "the news" digitado não substitui assinatura.
- A **caneca** (disco) pode aparecer isolada em ícone, favicon, app icon, avatar. **Sempre em degradê amarelo**, nunca outra cor.
- Liquid glass é permitido desde que não prejudique leitura.

### Forma e espaço
- Raios: **0** em cards, imagens e containers; **16px** em pílulas, botões e inputs; **50%** só em discos (caneca, avatar, ícone circular).
- Escala de espaço: 4, 8, 16, 32, 56, 108 (ver tokens). Não invente valores intermediários.
- **Tarja degradê** (laranja → amarelo, ponta a ponta) é o elemento-assinatura: use no pé de headers, footers, heros e telas cheias. Altura 4 a 8px em UI densa, 20px em hero/slide.
- Sombras: praticamente nenhuma. A marca é plana; hierarquia vem de cor, peso e espaço.

### Texto (resumo; detalhes em `references/voz-e-texto.md`)
- **minúscula** no início de títulos, botões, labels, menus, toasts e microcopy. Nomes próprios mantêm maiúscula.
- **o** the news (artigo masculino). Nunca "a the news".
- **travessão (—)**, nunca meia-risca (–) nem hífen como pausa.
- Emoji só no início ou no fim da frase.
- Tom: direto, próximo, irônico na medida, nunca complexo. "10 linhas o que outros dizem em 50".
- Conteúdo patrocinado é **sempre** sinalizado ("powered by", "patrocinado"). Nunca disfarçar anúncio de matéria.
- Imparcialidade: a UI não toma lado político (cores de partido, rótulos opinativos).

## Checklist antes de entregar
- [ ] Só variáveis de `tokens.css`; zero hex solto fora dele.
- [ ] Nenhum texto amarelo ou laranja sobre fundo claro.
- [ ] Logo é arquivo original, na versão certa para o fundo.
- [ ] Títulos 700/900 com tracking -0.02em; corpo 300/400.
- [ ] Cards retos, pílulas/botões 16px.
- [ ] Textos em minúscula, "o the news", travessão correto, emoji na ponta.
- [ ] Dark mode via tokens (`[data-theme="dark"]` / `prefers-color-scheme`).
- [ ] Contraste AA (texto ≥ 4.5:1) e foco visível.
- [ ] `scripts/check_brand.py` sem erros.

## Quando a regra não cobre
Escolha a opção mais simples, mais clara e com menos elementos. Se ainda houver dúvida, preto sobre branco com um único destaque amarelo é sempre seguro.
