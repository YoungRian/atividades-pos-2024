import requests
from getpass import getpass

# API do SUAP
api_url = "https://suap.ifrn.edu.br/api/"

user = input("Usuário (Matrícula): ")
password = getpass("Senha: ")

data = {"username": user, "password": password}

response = requests.post(api_url + "v2/autenticacao/token/", json=data)
if response.status_code != 200:
    print("Erro ao autenticar. Verifique suas credenciais.")
    exit()

token = response.json()["access"]

headers = {
    "Authorization": f"Bearer {token}"
}

# Envia a requisição para obter o boletim do aluno
response = requests.get(api_url + "v2/minhas-informacoes/boletim/", headers=headers)
if response.status_code != 200:
    print("Erro ao obter o boletim. Verifique sua conexão e permissões.")
    exit()

# Carega os dados do boletim
boletim = response.json()

# Mostra o boletim formatado do aluno
print("\nBoletim do Aluno:")
for disciplina in boletim:
    nome = disciplina["disciplina"]
    unidade1 = disciplina.get("nota_unidade_1", "-")
    unidade2 = disciplina.get("nota_unidade_2", "-")
    unidade3 = disciplina.get("nota_unidade_3", "-")
    unidade4 = disciplina.get("nota_unidade_4", "-")
    media_final = disciplina.get("media_final", "-")
    print(
        f"Disciplina: {nome}\n"
        f"1ª Unidade: {unidade1}, 2ª Unidade: {unidade2}, "
        f"3ª Unidade: {unidade3}, 4ª Unidade: {unidade4}, Média Final: {media_final}\n"
    )
