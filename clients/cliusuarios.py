import requests

api_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url)

#print(response.json())

if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
    todos = response.json()  # Converte a resposta para um objeto Python
    print(todos)
else:
    print(f"Erro na requisição: {response.status_code}")
    
def listar_todos_os_usuarios(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(f"ID: {usuario['id']} | Nome: {usuario['name']} | Email: {usuario['email']}")
    else:
        print(f"Erro ao listar os usuários: {response.status_code}")

def listar_tarefas_usuario(api_url, user_id):
    todos_url = f"{api_url}/{user_id}/todos"
    response = requests.get(todos_url)
    if response.status_code == 200:
        tarefas = response.json()
        if tarefas:
            for tarefa in tarefas:
                status = "Concluída" if tarefa['completed'] else "Pendente"
                print(f"Tarefa ID: {tarefa['id']} | Título: {tarefa['title']} | Status: {status}")
        else:
            print("Este usuário não possui tarefas.")
    else:
        print(f"Erro ao listar tarefas: {response.status_code}")

def criar_usuario(api_url):
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    dados = {"name": nome, "email": email}
    response = requests.post(api_url, json=dados)
    if response.status_code == 201:
        print("Usuário criado com sucesso:", response.json())
    else:
        print(f"Erro ao criar usuário: {response.status_code}")

def ler_usuario(api_url, user_id):
    response = requests.get(f"{api_url}/{user_id}")
    if response.status_code == 200:
        usuario = response.json()
        print(f"ID: {usuario['id']} | Nome: {usuario['name']} | Email: {usuario['email']}")
    else:
        print(f"Erro ao ler usuário: {response.status_code}")

def atualizar_usuario(api_url, user_id):
    nome = input("Digite o novo nome do usuário: ")
    email = input("Digite o novo email do usuário: ")
    dados = {"name": nome, "email": email}
    response = requests.put(f"{api_url}/{user_id}", json=dados)
    if response.status_code == 200:
        print("Usuário atualizado com sucesso:", response.json())
    else:
        print(f"Erro ao atualizar usuário: {response.status_code}")

def deletar_usuario(api_url, user_id):
    response = requests.delete(f"{api_url}/{user_id}")
    if response.status_code == 200:
        print("Usuário deletado com sucesso.")
    else:
        print(f"Erro ao deletar usuário: {response.status_code}")

def main():
    api_url = "https://jsonplaceholder.typicode.com/users"
    while True:
        print("\nOpções:")
        print("1. Listar todos os usuários")
        print("2. Listar as tarefas de um usuário específico")
        print("3. Criar um novo usuário")
        print("4. Ler os dados de um usuário específico")
        print("5. Atualizar um usuário existente")
        print("6. Deletar um usuário")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_todos_os_usuarios(api_url)
        elif opcao == "2":
            user_id = input("Digite o ID do usuário: ")
            listar_tarefas_usuario(api_url, user_id)
        elif opcao == "3":
            criar_usuario(api_url)
        elif opcao == "4":
            user_id = input("Digite o ID do usuário: ")
            ler_usuario(api_url, user_id)
        elif opcao == "5":
            user_id = input("Digite o ID do usuário: ")
            atualizar_usuario(api_url, user_id)
        elif opcao == "6":
            user_id = input("Digite o ID do usuário: ")
            deletar_usuario(api_url, user_id)
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
