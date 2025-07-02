# microservico

🚀 Como Executar Localmente
1. Clone o repositório
Abra o terminal e execute os comandos:

bash
Copiar
Editar
git clone https://github.com/Samuel-Dinho/microservico.git
cd cep-microservice

2. Configure o Ambiente Virtual (Opcional, mas recomendado)
É uma boa prática isolar as dependências do projeto utilizando um ambiente virtual.

Crie o ambiente virtual:
python -m venv venv

Ative o ambiente virtual:

Windows (CMD/PowerShell):
.\venv\Scripts\activate

3. Instale as dependências
Com o ambiente virtual ativado, instale todas as dependências necessárias com o comando:


pip install -r requirements.txt

4. Execute o microserviço
Inicie o serviço localmente executando:


python app.py