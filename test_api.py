import requests

# Substitua pela URL e chave de autenticação da sua API Exchange Rate
url = "https://api.exchangerate-api.com/v4/latest/USD"  # USD como exemplo de moeda base
api_key = "a844cafe5af2868a20e10eb3"  # Substitua pela sua chave válida

# Realiza a requisição para a API
response = requests.get(f"{url}?apikey={api_key}")

# Exibe o resultado
if response.status_code == 200:
    print("Conexão bem-sucedida!")
    print(response.json())  # Imprime o JSON com as taxas de câmbio
else:
    print("Erro ao conectar à API.")
    print(f"Status Code: {response.status_code}, Resposta: {response.text}")
