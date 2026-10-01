import requests
from bs4 import BeautifulSoup

# Coloque aqui o site que você escolheu
URL = "https://exemplo.com/bitcoin"

# Seletor CSS do preço (veja em "Inspecionar" no navegador)
SELETOR = "span.preco"


def baixar_pagina():
    resposta = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    resposta.raise_for_status()
    return resposta.text


def extrair_preco(html):
    sopa = BeautifulSoup(html, "html.parser")
    elemento = sopa.select_one(SELETOR)
    if elemento is None:
        raise ValueError("Preço não encontrado. Confira a URL e o seletor.")

    texto = elemento.get_text(strip=True)   # exemplo: "$67,000.12"
    texto = texto.replace("$", "").replace(",", "")
    return float(texto)
