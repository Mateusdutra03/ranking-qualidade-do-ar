
# 🌍 Ranking de Qualidade do Ar

Este script Python consulta a qualidade do ar (AQI - Air Quality Index) de 10 grandes cidades do mundo usando a API do [World Air Quality Index](https://waqi.info/) e exibe um ranking ordenado da melhor para a pior qualidade do ar.

## 📄 Descrição

O script realiza:

- Consulta da qualidade do ar de cidades como Beijing, New York, London, Paris, Tokyo, entre outras.
- Organização dos dados em um ranking baseado no AQI (quanto menor, melhor).
- Impressão dos resultados em formato de tabela no terminal.

## 🚀 Como usar

1. Clone este repositório ou baixe o arquivo `ranking_qualidade_ar.py`.

2. Instale as dependências (se necessário):

```bash
pip install requests
```

3. Obtenha uma **API Key gratuita** em [https://aqicn.org/data-platform/token/](https://aqicn.org/data-platform/token/).

4. Substitua o valor da variável `token` no script pelo seu token da API:

```python
token = "SUA_API_KEY_AQUI"
```

5. Execute o script:

```bash
python ranking_qualidade_ar.py
```

## 🧪 Exemplo de saída

```
Ranking de Qualidade do Ar:
Cidade          AQI  
-------------------------
Sydney          23   
Berlin          34   
London          42   
...
Beijing         157  
```

## 🛠️ Tecnologias

- Python 3.x
- Biblioteca `requests`
- API do World Air Quality Index

## 📌 Observações

- Os dados retornados estão sujeitos à disponibilidade da API e à estabilidade da conexão com a internet.
- O valor de AQI pode variar ao longo do dia. Os dados refletem o momento da consulta.

## 📞 Contato

Este projeto foi desenvolvido pela [Digital Quanta](https://digitalquanta.com.br). Para consultoria, soluções com inteligência artificial ou desenvolvimento personalizado, entre em contato através do nosso site.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
