from flask import Flask, jsonify
import requests

app = Flask(__name__)


API_KEY = "a844cafe5af2868a20e10eb3"

@app.route('/currencies', methods=['GET'])
def get_currencies():
    # URL para obter a lista de moedas
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
    response = requests.get(url)
    
    # Se a resposta for bem-sucedida, retorna os dados em JSON
    if response.status_code == 200:
        currency_data = response.json()
        return jsonify(currency_data)
    else:
        # Em caso de erro, retorna uma mensagem de erro
        return jsonify({"error": response.json().get("error-type", "Unknown error")}), response.status_code

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
