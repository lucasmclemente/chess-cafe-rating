# Rating do Chess Café

Dashboard público de rating dos alunos, gerado a partir da planilha `RATING OFICIAL.xlsx`.

```
planilha.xlsx  →  python gerar.py  →  docs/index.html  →  GitHub Pages
```

## Uso no dia a dia

1. Lance as partidas na aba **PARTIDAS** da planilha (Jogador A, Jogador B, Resultado) e salve.
2. Rode:

```bash
cd C:\Users\lucas\projetos\rating-xadrez && python gerar.py
```

3. Publique (depois que o GitHub estiver configurado — veja abaixo):

```bash
cd C:\Users\lucas\projetos\rating-xadrez && git add -A && git commit -m "Atualiza rating" && git push
```

O site atualiza em cerca de um minuto.

## Arquivos

| Arquivo | O que faz |
|---|---|
| `elo.py` | Lê a planilha e recalcula o rating partida a partida |
| `gerar.py` | Monta o `docs/index.html` com os dados embutidos |
| `modelo.html` | O visual do dashboard (edite aqui para mudar cores e layout) |
| `config.txt` | Caminho da planilha |
| `exemplo.py` | Cria uma planilha fictícia, para ver o dashboard funcionando sem dados reais |
| `docs/index.html` | O site publicado |

Para pré-visualizar com dados fictícios:

```bash
cd C:\Users\lucas\projetos\rating-xadrez && python exemplo.py && python gerar.py exemplo.xlsx
```

Depois é só rodar `python gerar.py` de novo para voltar aos dados reais.

## Como o rating é calculado

Replica exatamente as fórmulas da planilha:

- Rating de estreia: **1500** para quem não tem "Rating Inicial" na aba RATING
- Fator **K = 40**
- `esperado = 1 / (1 + 10^((rating_adversário − rating_jogador) / 400))`
- `variação = arredonda(40 × (pontuação − esperado))`, e o adversário recebe o valor com sinal invertido

O cálculo é refeito em Python a partir das partidas, não lido das células. Assim o dashboard funciona mesmo se você abrir a planilha no LibreOffice ou no Google Sheets, que não deixam valores calculados em cache.

## Coluna de data (opcional)

A planilha hoje não registra **quando** cada partida foi jogada, então a evolução aparece por número de partida ("partida 1, 2, 3…").

Se quiser datas no gráfico, adicione uma coluna com o cabeçalho **`Data`** na aba PARTIDAS. O `gerar.py` reconhece a coluna pelo nome e passa a exibi-la — não precisa mexer no código. As outras colunas podem ficar onde estão.

## Publicar no GitHub Pages

Só precisa ser feito uma vez.

1. Crie uma conta em [github.com](https://github.com) (se ainda não tiver) e um repositório novo — pode se chamar `chess-cafe-rating`. Deixe-o **público**.
2. Na pasta do projeto:

```bash
cd C:\Users\lucas\projetos\rating-xadrez && git init -b main && git add -A && git commit -m "Dashboard de rating do Chess Cafe"
```

3. Conecte ao repositório que você criou (troque `SEU-USUARIO`):

```bash
git remote add origin https://github.com/SEU-USUARIO/chess-cafe-rating.git && git push -u origin main
```

4. No GitHub, vá em **Settings → Pages**, e em "Source" escolha **Deploy from a branch**, branch `main`, pasta **`/docs`**. Salve.

O link ficará `https://SEU-USUARIO.github.io/chess-cafe-rating/` — é esse que você manda para os alunos.

> A planilha **não** vai para o GitHub (está no `.gitignore`). Só o site gerado é publicado.
