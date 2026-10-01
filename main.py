import scraper


def main():
    html = scraper.baixar_pagina()
    print(f"Página baixada: {len(html)} caracteres")


if __name__ == "__main__":
    main()
