import csv
import os
from datetime import date

PASTA = "data"
ARQUIVO = os.path.join(PASTA, "cotacoes.csv")


def salvar(preco):
    os.makedirs(PASTA, exist_ok=True)
    arquivo_novo = not os.path.exists(ARQUIVO)

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if arquivo_novo:
            escritor.writerow(["data", "preco"])
        escritor.writerow([date.today().isoformat(), preco])
