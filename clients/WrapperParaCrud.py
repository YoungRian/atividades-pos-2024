# Wrapper para o CRUD da API dos usuarios
import requests

class UsersWrapper:
    def __init__(self, api_url):
        self.api_url = api_url

    def list(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao listar usuários: {response.status_code}")

    def create(self, name, email):
        data = {"name": name, "email": email}
        response = requests.post(self.api_url, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Erro ao criar usuário: {response.status_code}")

    def read(self, user_id):
        response = requests.get(f"{self.api_url}/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao ler usuário: {response.status_code}")

    def update(self, user_id, name, email):
        data = {"name": name, "email": email}
        response = requests.put(f"{self.api_url}/{user_id}", json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao atualizar usuário: {response.status_code}")

    def delete(self, user_id):
        response = requests.delete(f"{self.api_url}/{user_id}")
        if response.status_code == 200:
            return {"message": "Usuário deletado com sucesso."}
        else:
            raise Exception(f"Erro ao deletar usuário: {response.status_code}")

# CLI que utiliza a biblioteca UsersWrapper
def main():
    api_url = "https://jsonplaceholder.typicode.com/users"
    users = UsersWrapper(api_url)

    while True:
        print("\nOpções:")
        print("1. Listar todos os usuários")
        print("2. Criar um novo usuário")
        print("3. Ler os dados de um usuário específico")
        print("4. Atualizar um usuário existente")
        print("5. Deletar um usuário")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                usuarios = users.list()
                for usuario in usuarios:
                    print(f"ID: {usuario['id']} | Nome: {usuario['name']} | Email: {usuario['email']}")
            elif opcao == "2":
                name = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                novo_usuario = users.create(name, email)
                print("Usuário criado com sucesso:", novo_usuario)
            elif opcao == "3":
                user_id = input("Digite o ID do usuário: ")
                usuario = users.read(user_id)
                print(f"ID: {usuario['id']} | Nome: {usuario['name']} | Email: {usuario['email']}")
            elif opcao == "4":
                user_id = input("Digite o ID do usuário: ")
                name = input("Digite o novo nome do usuário: ")
                email = input("Digite o novo email do usuário: ")
                usuario_atualizado = users.update(user_id, name, email)
                print("Usuário atualizado com sucesso:", usuario_atualizado)
            elif opcao == "5":
                user_id = input("Digite o ID do usuário: ")
                mensagem = users.delete(user_id)
                print(mensagem["message"])
            elif opcao == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
