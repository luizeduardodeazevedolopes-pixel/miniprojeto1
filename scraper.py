import requests

# Coloque aqui o site que você escolheu
URL = "https://exemplo.com/bitcoin"


def baixar_pagina():
    resposta = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    resposta.raise_for_status()
    return resposta.text
