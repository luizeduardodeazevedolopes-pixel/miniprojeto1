# 🪙 Bitcoin Tracker

Mini projeto de *web scraping* em Python que busca a cotação do bitcoin e guarda o histórico em um arquivo CSV, pensado para rodar semanalmente.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📌 Sobre

O programa baixa a página de um site de cotações, extrai o preço atual do bitcoin e acrescenta uma linha (data e valor) em `data/cotacoes.csv`.

Projeto desenvolvido para a disciplina de Linguagem de Programação II (Fatec Rio Claro).

**Fonte dos dados:"https://dolarhoje.com/bitcoin-hoje/"_

## 🛠️ Tecnologias

- Python 3
- `requests`: baixa as páginas
- `beautifulsoup4`: analisa o HTML e extrai o preço
- `webbrowser`: abre a página da cotação no navegador

## ⚙️ Instalação

```bash
git clone <url-do-repositorio>
cd bitcoin-tracker
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
```

## ▶️ Como usar

```bash
python main.py            # busca a cotação e salva no CSV
python main.py --abrir    # além disso, abre o site no navegador
```

_[preencher: exemplo do que o programa imprime]_

## 🗓️ Execução semanal

_[preencher: como você agendou (Agendador de Tarefas, cron ou GitHub Actions)]_

## 📂 Estrutura do projeto

```
bitcoin-tracker/
├── main.py          # junta as etapas
├── scraper.py       # baixa a página e extrai o preço
├── storage.py       # registra as cotações no CSV
├── data/
│   └── cotacoes.csv # histórico (gerado pelo programa)
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚠️ Aviso

Respeite os termos de uso e o `robots.txt` do site consultado.

## 👤 Autor

Luiz — https://github.com/luizeduardodeazevedolopes-pixel
