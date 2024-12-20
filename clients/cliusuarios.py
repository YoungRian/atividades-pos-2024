import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)

print(response.json())

if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
    todos = response.json()  # Converte a resposta para um objeto Python
    print(todos)
else:
    print(f"Erro na requisição: {response.status_code}")