import scraper


def main():
    html = scraper.baixar_pagina()
    preco = scraper.extrair_preco(html)
    print(f"Bitcoin: {preco:.2f}")


if __name__ == "__main__":
    main()
