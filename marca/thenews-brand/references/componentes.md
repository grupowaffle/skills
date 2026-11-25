# componentes de UI — the news

Tradução dos layouts do brandbook (slides) para interface. Todos usam variáveis de `tokens.css`.

## Sumário
1. tarja degradê · 2. header/footer · 3. botões · 4. inputs · 5. pílula de número · 6. card preto de número · 7. eyebrow · 8. highlight (marca-texto) · 9. cards de conteúdo · 10. layout dividido · 11. hero/manifesto · 12. termômetro · 13. tabela · 14. badges e patrocínio · 15. ícones, avatar, favicon · 16. grafismo · 17. estados

---

## 1. tarja degradê
Elemento-assinatura. Faixa laranja → amarelo, esquerda → direita, ponta a ponta.
```css
.tn-tarja { height: var(--tarja); background: var(--tn-degrade); width: 100%; }
.tn-tarja--hero { height: var(--tarja-hero); }
```
Onde: base do header, topo ou base do footer, pé de hero, pé de email. Uma por tela visível é suficiente. Em submarca troque por `--sub-degrade`.

## 2. header / footer
- Header: fundo `--surface`, logo completo à esquerda (altura 28 a 36px), nav em 400/700 minúscula, tarja embaixo.
- Footer: fundo `--tn-preto`, `the-news-branco.png`, links em branco 300, `© 2026 tns` em `--ink-muted` do tema escuro. Símbolo `tns` pode ir pequeno no canto inferior direito (como nos slides).
- Nunca logo em texto. Sempre `<img src="the-news-preto.png" alt="the news">`.

## 3. botões
| variante | fundo | texto | uso |
|---|---|---|---|
| primário | `--tn-amarelo` | preto 700 | 1 CTA principal por tela |
| secundário | `--tn-preto` | branco 700 | ação forte sem competir com o amarelo |
| terciário | transparente, borda 1.5px `--line` | `--ink` 700 | ações neutras |
| texto | nenhum | `--ink` 700, sublinhado no hover | links de ação |

```css
.tn-btn { font: 700 1rem/1 var(--font-display); letter-spacing: -0.01em; padding: 14px 24px; border-radius: var(--radius-pill); border: 0; cursor: pointer; }
.tn-btn--primario { background: var(--tn-amarelo); color: var(--tn-preto); }
.tn-btn--primario:hover { background: var(--tn-degrade); }
.tn-btn--secundario { background: var(--tn-preto); color: var(--tn-branco); }
.tn-btn--terciario { background: transparent; color: var(--ink); box-shadow: inset 0 0 0 1.5px var(--line); }
.tn-btn:disabled { opacity: .4; cursor: not-allowed; }
```
Rótulo em minúscula, verbo direto: "assinar grátis", "ler edição de hoje". Sem ícone decorativo; seta → só se indicar navegação.
No tema escuro o primário continua amarelo com texto preto.

## 4. inputs
Fundo `--surface`, borda 1.5px `--line-soft`, foco em borda `--line` + outline `--focus`, raio 16px, label acima em 700 `--fs-small` minúscula. Placeholder `--ink-muted`. Erro: borda `--feedback-erro` + mensagem em `--ink` com ícone vermelho.

## 5. pílula de número
Número grande dentro de pílula amarela; rótulo em Bold preto abaixo.
```css
.tn-pilula { background: var(--tn-amarelo); color: var(--tn-preto); border-radius: var(--radius-pill); padding: 12px 32px; font: 900 var(--fs-numero)/1 var(--font-display); letter-spacing: var(--tracking-titulo); display: inline-block; }
.tn-pilula + .tn-rotulo { margin-top: var(--space-1); font-weight: 700; }
```

## 6. card preto de número
Card preto de **cantos retos**: eyebrow amarelo caixa alta, número branco 900, texto branco 300, fonte entre parênteses abaixo do card em `--ink-muted`.
```css
.tn-card-numero { background: var(--tn-preto); color: var(--tn-branco); border-radius: 0; padding: var(--space-2); }
.tn-card-numero .tn-eyebrow { color: var(--tn-amarelo); }
```

## 7. eyebrow
Rótulo curto em CAIXA ALTA (uma das exceções à minúscula), 800, `--fs-eyebrow`, tracking 0.04em.
- Sobre preto: texto amarelo.
- Sobre claro: texto preto + barra amarela 4px à esquerda (`border-left: 4px solid var(--tn-amarelo); padding-left: 8px`).

## 8. highlight (marca-texto)
Como nas newsletters ("Descubra:", "Para ler:"): fundo amarelo atrás do texto preto.
```css
.tn-highlight { background: var(--tn-amarelo); color: var(--tn-preto); padding: 0 .2em; font-weight: 700; box-decoration-break: clone; }
```

## 9. cards de conteúdo
Raio 0, sem sombra. Separação por `--surface-alt` de fundo **ou** linha preta fina no topo (padrão do brandbook: título pequeno + linha preta + conteúdo). Imagem retangular, raio 0. Título 700 minúsculo, resumo 300.

## 10. layout dividido
Painel `--surface-alt` à esquerda (~40%) com logo e texto 300; conteúdo no lado branco. Bom para login, onboarding, páginas institucionais. Em mobile, o painel vira topo.

## 11. hero / manifesto
- Hero claro: título `--fs-display` 900 minúsculo com ponto final, subtítulo `--fs-lead` 300, barra vertical amarela 8px à esquerda do título (como a capa). Tarja hero no pé.
- Manifesto: fundo preto, frase em CAIXA ALTA 900 centralizada, palavras-chave em amarelo. Uma frase só.
- Encerramento/celebração: fundo `--tn-degrade-vertical`, texto branco 900 ("thanks", "pronto.").

## 12. termômetro
Elemento proprietário (ex.: "termômetro de imparcialidade"): barra horizontal com disco à esquerda, preenchimento em degradê laranja → amarelo, trilho `--surface-alt`, valor em branco 900 sobre a barra e rótulo 700 acima. Use para progresso/percentual com significado editorial; para progresso comum (upload), barra simples preta.

## 13. tabela
Cabeçalho 700 minúsculo, linha preta 1.5px abaixo do cabeçalho, linhas `--line-soft` entre itens, números tabulares (`font-variant-numeric: tabular-nums`) alinhados à direita. Linha em destaque: fundo `--tn-amarelo` com texto preto. Sem zebra colorida.

## 14. badges e patrocínio
- Badge: pílula pequena, fundo amarelo ou preto, texto 700 `--fs-small`.
- Patrocínio é obrigatório e visível: "powered by" em eyebrow `--ink-muted` + logo do parceiro, separado do conteúdo editorial. Nunca estilize anúncio como matéria.

## 15. ícones, avatar, favicon
- Ícones: traço de 1.5 a 2px, monocromáticos em `--ink`. Sem ícones coloridos/ilustrados.
- Favicon / app icon: caneca (disco degradê amarelo) ou "t" com traço degradê, a partir dos arquivos oficiais.
- Avatar: círculo, raio 50%.

## 16. grafismo
Fundos de hero/capa podem usar o grafismo: manchas suaves amarelo → laranja → branco (radial-gradient com blur), sempre com texto preto ou branco legível por cima. Não use em telas de leitura ou formulários.
```css
.tn-grafismo { background: radial-gradient(120% 90% at 30% 80%, var(--tn-amarelo) 0%, var(--tn-laranja) 45%, transparent 75%), var(--surface); }
```

## 17. estados
- Vazio: frase curta, irônica na medida, minúscula ("nada por aqui. ainda."), um CTA.
- Carregando: skeleton em `--surface-alt`, sem shimmer colorido.
- Erro: diga o que houve e o que fazer, sem culpar o usuário.
- Sucesso: toast preto com texto branco, ícone verde opcional.
