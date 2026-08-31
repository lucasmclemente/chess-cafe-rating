import random
from openpyxl import Workbook
from pathlib import Path

random.seed(7)
nomes = ["Ana Souza", "Bruno Lima", "Carla Dias", "Diego Alves", "Elisa Rocha",
         "Felipe Nunes", "Gabi Martins", "Heitor Prado"]

wb = Workbook()
r = wb.active
r.title = "RATING"
r.append(["Jogador", "Rating Inicial", "Rating Atual", "Classificação"])
for i, n in enumerate(nomes):
    r.append([n, 1200 + i * 60])

p = wb.create_sheet("PARTIDAS")
p.append(["Nº", "Jogador A", "Jogador B", "Resultado", "Rating A", "Rating B", "Variação A", "Variação B"])
for i in range(60):
    a, b = random.sample(nomes, 2)
    p.append([i + 1, a, b, random.choice(["1-0", "0,5-0,5", "0-1"])])

destino = Path("exemplo.xlsx")
wb.save(destino)
print("planilha de teste criada:", destino)
