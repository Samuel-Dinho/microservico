from flask import Flask, jsonify
import requests

app = Flask(__name__)


VIACEP_API_URL = "https://viacep.com.br/ws/{}/json/"

@app.route('/cep/<string:cep>', methods=['GET'])
def get_endereco(cep):
    """
    Endpoint para consultar um CEP e retornar os dados de endereço.
    """
    
    cep = cep.replace('-', '').replace('.', '').strip()
    if not cep.isdigit() or len(cep) != 8:
        return jsonify({"erro": "CEP inválido. Use 8 dígitos numéricos."}), 400

    
    try:
        response = requests.get(VIACEP_API_URL.format(cep))
        response.raise_for_status()  
        data = response.json()

        
        if "erro" in data:
            return jsonify({"erro": "CEP não encontrado."}), 404
        
        
        address_info = {
            "cep": data.get("cep"),
            "logradouro": data.get("logradouro"),
            "complemento": data.get("complemento"),
            "bairro": data.get("bairro"),
            "localidade": data.get("localidade"), 
            "uf": data.get("uf") 
        }
        
        return jsonify(address_info), 200

    except requests.exceptions.RequestException as e:
        
        return jsonify({"erro": f"Erro ao conectar com o serviço de CEP: {str(e)}"}), 500
    except Exception as e:
        
        return jsonify({"erro": f"Um erro inesperado ocorreu: {str(e)}"}), 500

if __name__ == '__main__':
    
    
    app.run(debug=True, host='0.0.0.0', port=5000)