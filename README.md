🚀 Como Executar Localmente
Siga estes passos para colocar o microserviço funcionando na sua máquina:

1. Clone o repositório
Abra o terminal e execute os comandos:

Bash

git clone https://github.com/Samuel-Dinho/microservico.git
cd microservico # Ajustado para o nome do seu repositório
2. Configure o Ambiente Virtual (Opcional, mas recomendado)
É uma boa prática isolar as dependências do projeto utilizando um ambiente virtual.

Crie o ambiente virtual:

Bash

python -m venv venv
Ative o ambiente virtual:

Windows (CMD/PowerShell):

Bash

.\venv\Scripts\activate
Linux/macOS/Git Bash:

Bash

source venv/bin/activate
3. Instale as dependências
Com o ambiente virtual ativado, instale todas as dependências necessárias com o comando:

Bash

pip install -r requirements.txt
4. Execute o microserviço
Inicie o serviço localmente executando:

Bash

python app.py
O microserviço estará rodando em http://localhost:5000.

💡 Como Usar
Para consultar um CEP, faça uma requisição GET para a rota /cep/<seu_cep>.

Exemplo:

Para consultar o CEP 89201000 (Joinville, SC):

Bash

curl http://localhost:5000/cep/89201000
Resposta esperada (JSON):

JSON

{
  "cep": "89201-000",
  "logradouro": "Rua Princesa Isabel",
  "complemento": "",
  "bairro": "Centro",
  "localidade": "Joinville",
  "uf": "SC"
}