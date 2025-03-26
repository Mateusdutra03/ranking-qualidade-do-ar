import requests

# Substitua pelo seu token de API
token = "0775cec730484de5bcdf2e91d746ad0219f30bbd"

# Lista das 10 cidades para consulta
cidades = [
    "Beijing", "New York", "London", "Paris", "Tokyo", 
    "Moscow", "Sydney", "Los Angeles", "Delhi", "Berlin"
]

# Função para obter a qualidade do ar de uma cidade
def obter_qualidade_ar(cidade):
    url = f"https://api.waqi.info/feed/{cidade}/?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if dados.get("status") == "ok":
            aqi = dados["data"]["aqi"]  # Índice de Qualidade do Ar
            return aqi
        else:
            return None
    else:
        return None

# Lista para armazenar os resultados
resultados = []

# Obtendo a qualidade do ar para cada cidade
for cidade in cidades:
    aqi = obter_qualidade_ar(cidade)
    if aqi is not None:
        resultados.append((cidade, aqi))
    else:
        resultados.append((cidade, "Erro na consulta"))

# Ordenando os resultados pela qualidade do ar (AQI)
resultados_ordenados = sorted(resultados, key=lambda x: x[1] if isinstance(x[1], int) else float('inf'))

# Exibindo o ranking
print("Ranking de Qualidade do Ar:")
print(f"{'Cidade':<15} {'AQI':<5}")
print("-" * 25)
for cidade, aqi in resultados_ordenados:
    print(f"{cidade:<15} {aqi:<5}")
