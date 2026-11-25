# submarcas — the news

Arquitetura: **tns** (grupo) → newsletter **the news** + submarcas · podcasts · programas (morning) · ventures (rising, little bean).

## estrutura fixa (não variar)
Logo de submarca = traço degradê da submarca + "the news" em preto (ou branco) + nome da submarca em CAIXA ALTA 900 com degradê das cores da submarca, alinhado à direita embaixo. A **tarja degradê é obrigatória**; a marca-mãe não precisa aparecer sempre. Não crie variações estruturais.

Os logos oficiais estão em `assets/logos/horizontal/<NOME>.png` (assinatura) e `assets/logos/icons/<nome>.png` (ícone quadrado com o "t" e o traço da submarca). **Não recrie** em CSS/SVG.

- Os horizontais têm "the news" em preto: servem só para fundo claro. Não há versão para fundo escuro no pacote; se precisar, peça ao time de marca em vez de inverter as cores.
- Sem ícone no pacote: travel e better work. Sem horizontal: rising (só `icons/rising.png`, em baixa resolução).

## paleta (degradê vai da cor 1 para a cor 2)
| submarca | cor 1 | cor 2 | observação |
|---|---|---|---|
| morning | #ff8e42 | #ffcd00 | mesmo degradê da marca-mãe |
| night | #000000 | #374b84 | |
| money | #2aa0a7 | #00bf63 | |
| trends | #f70301 | #f97f2e | |
| business | #3632ca | #f742a1 | |
| sports | #760102 | #f70301 | |
| health | #6a98ff | #94eeff | |
| around | #4f5025 | #d9c8ba | |
| travel | #000000 | #9a9a9a | |
| cult | #dc4659 | #f4b0b2 | |
| elections | #1906ae | #6c9bf7 | |
| better work | — | — | logo em `assets/logos/horizontal/BETTERWORK.png` (azul em degradê); sem hex oficial, confirmar com marca |

## como aplicar em UI
- Envolva a área em `data-brand="money"` (etc.) e use `--sub-1`, `--sub-2`, `--sub-degrade`.
- Cores de submarca substituem o amarelo **só** nos acentos: tarja, traço, eyebrow, highlight, botão primário. Estrutura, tipografia, raios e voz continuam os da marca-mãe.
- Contraste: confira cada uso. Cores claras (health #94eeff, around #d9c8ba, cult #f4b0b2, travel #9a9a9a, money #00bf63) **não** servem como texto sobre branco; use-as como fundo com texto preto. Cores escuras (night #374b84, sports #760102, elections #1906ae, business #3632ca, around #4f5025) servem como fundo com texto branco.
- Nunca misture duas submarcas na mesma peça, salvo vitrines que listam todas (ex.: página de newsletters), onde cada card leva só a cor da sua.
