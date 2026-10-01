import sys
import webbrowser

import scraper
import storage


def main():
    try:
        html = scraper.baixar_pagina()
        preco = scraper.extrair_preco(html)
    except Exception as erro:
        print(f"Erro ao buscar a cotação: {erro}")
        return

    storage.salvar(preco)
    print(f"Bitcoin: {preco:.2f}")

    # python main.py --abrir  -> abre o site no navegador
    if "--abrir" in sys.argv:
        webbrowser.open(scraper.URL)


if __name__ == "__main__":
    main()
