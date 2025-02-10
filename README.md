# Online Grocery Ordering Automation

Este projeto automatiza o processo de preenchimento e envio de uma lista de compras em uma página web específica. Utiliza Selenium para automação do navegador, manipulação de arquivos CSV e uso de variáveis de ambiente para login seguro.

## Descrição do Código

O script principal (`main.py`) faz o seguinte:
- Configura o Selenium WebDriver para navegar na página web.
- Realiza o login no Automation Anywhere Community utilizando credenciais armazenadas no arquivo `.env`.
- Carrega uma lista de compras de um arquivo CSV.
- Preenche e envia a lista de compras na página web.
- Captura e registra os resultados da execução.

## Requisitos

- Python 3.x
- Selenium
- python-dotenv
- Pandas

## Estrutura do Projeto

```
OnlineGroceryOrderingAutomation/
├── data/
│   └── shopping-list.csv
├── logs/
├── src/
│   ├── utils/
│   │   ├── aa_login.py
│   │   ├── custom_log.py
│   │   └── data_utils.py
│   └── main.py
└── .env
└── .gitignore
```
