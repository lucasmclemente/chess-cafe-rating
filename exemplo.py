"""Cria uma planilha ficticia, para ver o dashboard funcionando antes de ter dados reais.

Usa nomes inventados de proposito - nunca os dos alunos - para ninguem confundir
uma previa com resultado de verdade.

    python exemplo.py && python gerar.py exemplo.xlsx --saida previa.html
"""
import random
from pathlib import Path

from openpyxl import Workbook

random.seed(20)

# nome ficticio -> forca relativa, so para as partidas simuladas nao sairem no puro acaso
ELENCO = {
    "Alice Ferraz": 0.72,
    "Bento Aguiar": 0.62,
    "Clara Modesto": 0.55,
    "Davi Quintela": 0.45,
    "Estela Varjão": 0.36,
    "Fabio Trindade": 0.30,
}
PARTIDAS = 42


def resultado(forca_a, forca_b):
    """Sorteia 1-0, empate ou 0-1 com base na diferenca de forca."""
    chance_a = forca_a / (forca_a + forca_b)
    sorteio = random.random()
    if sorteio < 0.18:
        return "0,5-0,5"
    return "1-0" if random.random() < chance_a else "0-1"


wb = Workbook()

rating = wb.active
rating.title = "RATING"
rating.append(["Jogador", "Rating Inicial", "Rating Atual", "Classificação"])
for nome in ELENCO:
    rating.append([nome, 1500])

partidas = wb.create_sheet("PARTIDAS")
partidas.append(["Nº", "Jogador A", "Jogador B", "Resultado",
                 "Rating A", "Rating B", "Variação A", "Variação B"])
for n in range(1, PARTIDAS + 1):
    a, b = random.sample(list(ELENCO), 2)
    partidas.append([n, a, b, resultado(ELENCO[a], ELENCO[b])])

destino = Path(__file__).parent / "exemplo.xlsx"
wb.save(destino)
print(f"  planilha de exemplo criada: {destino}")
print(f"  {len(ELENCO)} jogadores ficticios | {PARTIDAS} partidas")
