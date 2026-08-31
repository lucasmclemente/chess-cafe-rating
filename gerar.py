#!/usr/bin/env python3
"""Gera o dashboard de rating do Chess Cafe.

Uso:
    python gerar.py                       # usa o caminho salvo em config.txt
    python gerar.py "C:/caminho/planilha.xlsx"

Saida: docs/index.html - um arquivo unico, sem dependencias externas.
"""
import json
import sys
from datetime import datetime
from pathlib import Path

from elo import calcular, ler_planilha

RAIZ = Path(__file__).parent
CONFIG = RAIZ / "config.txt"
SAIDA = RAIZ / "docs" / "index.html"


def caminho_planilha():
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    if CONFIG.exists():
        linha = CONFIG.read_text(encoding="utf-8").strip()
        if linha:
            return Path(linha)
    raise SystemExit(
        "Nao sei onde esta a planilha.\n"
        "  Rode:  python gerar.py \"C:/caminho/RATING OFICIAL.xlsx\"\n"
        f"  ou escreva o caminho no arquivo {CONFIG}"
    )


def main():
    planilha = caminho_planilha()
    if not planilha.exists():
        raise SystemExit(f"Planilha nao encontrada: {planilha}")

    iniciais, partidas, avisos = ler_planilha(planilha)
    jogadores = calcular(iniciais, partidas)

    for aviso in avisos:
        print(f"  aviso: {aviso}")

    ativos = [j for j in jogadores if j["partidas"] > 0]
    dados = {
        "gerado_em": datetime.now().strftime("%d/%m/%Y as %H:%M"),
        "total_jogadores": len(jogadores),
        "total_partidas": len(partidas),
        "rating_medio": round(sum(j["rating"] for j in ativos) / len(ativos)) if ativos else 0,
        "jogadores": jogadores,
    }

    modelo = (RAIZ / "modelo.html").read_text(encoding="utf-8")
    json_seguro = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    html = modelo.replace("__DADOS__", json_seguro)

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(html, encoding="utf-8")

    print(f"\n  {len(jogadores)} jogadores | {len(partidas)} partidas")
    print(f"  gerado: {SAIDA}")
    if not partidas:
        print("\n  A planilha ainda nao tem partidas - o dashboard saiu vazio.")


if __name__ == "__main__":
    main()
