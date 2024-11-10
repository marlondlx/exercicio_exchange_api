import requests
import json

def get_currency_list():
    url = "https://v6.exchangerate-api.com/v6/a844cafe5af2868a20e10eb3/codes"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Retorna o JSON com a lista de moedas
        return response.json()
    else:
        # Caso ocorra algum erro, retorna a mensagem de erro
        return {"error": response.json().get("error-type", "Unknown error")}

# Exemplo de chamada
currency_list = get_currency_list()
print(currency_list)
print(json.dumps(currency_list, indent=4))

