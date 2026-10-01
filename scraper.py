import requests
from bs4 import BeautifulSoup

# Site de cotação brasileiro
URL = "https://dolarhoje.com/bitcoin-hoje/"

# O Dólar Hoje armazena o valor do bitcoin em reais num campo de input com id "nacional"
SELETOR = "#nacional"


def baixar_pagina():
    # O cabeçalho User-Agent ajuda a evitar bloqueios por parte do site
    resposta = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    resposta.raise_for_status()
    return resposta.text


def extrair_preco(html):
    sopa = BeautifulSoup(html, "html.parser")
    elemento = sopa.select_one(SELETOR)

    if elemento is None:
        raise ValueError("Preço não encontrado. Confira a URL e o seletor.")

    # O valor numérico fica no atributo 'value' da tag <input>
    texto = elemento.get("value")  # Exemplo: "432.314,64"

    # Tratamento para o padrão brasileiro:
    # 1. Remove os pontos separadores de milhar
    # 2. Troca a vírgula decimal por ponto (padrão do Python)
    texto = texto.replace(".", "").replace(",", ".")

    return float(texto)