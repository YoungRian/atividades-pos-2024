import json

#Carrega os dados do arquivo JSON.
def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding='utf-8') as file:
        dados = json.load(file)
        return dados

dados = carregar_dados_json("json/imobiliaria2.json")

#Acessar elementos json
def mostrar_imoveis():
    for imovel in dados:
        print("--- Imovel ---")
        print(f"ID: {imovel['id']}")
        print(f"Descrição: {imovel['descricao']}")

#Função que irar acessar informações de acordo com o ID que o usuario forneceu.
def escolher_imovel():
    while True:
        #Busca ID do imovel
        imovel_id = input("Digite o ID do imovel (ou SAIR p/ encerrar): ".strip())
        #Se caso o usuario digitar 'sair' o programa vai encerrar.
        if imovel_id.lower() == "sair":
            print("Programa Encerrado")
            break
        
        #Por enquanto não tem nenhum valor id armazenado no imovel_encontrado.
        imovel_encontrado = None

        for imovel in dados:
            #Se o imovel for encontrado ele sera armazenado em imovel_encontrado.
            if imovel["id"] == imovel_id:
                imovel_encontrado = imovel
                break
        #Se caso o imovel for encontrado ira mostrar as informações.        
        if imovel_encontrado:
            print("\n--- Detalhes do Imóvel ---")
            print(f"ID: {imovel['id']}")
            print(f"Descrição: {imovel['descricao']}")
            print(f"Proprietário: {imovel['proprietario']['nome']}")
            print(f"Email: {imovel['proprietario']['email']}")
            print(f"Telefones: {', '.join(imovel['proprietario']['telefones'])}")
            print(f"Endereço: {imovel['endereco']['rua']}, {imovel['endereco']['numero']} - {imovel['endereco']['bairro']}, {imovel['endereco']['cidade']}")
            print(f"Tamanho: {imovel['caracteristicas']['tamanho']}")
            print(f"Número de Quartos: {imovel['caracteristicas']['numero de quartos']}")
            print(f"Número de Banheiros: {imovel['caracteristicas']['numero de banheiros']}")
            print(f"Valor: {imovel['valor']}")
        
        #Se caso não for encontrado.
        else:
            print(f"O Imovel com ID: {imovel_id} não foi encontrado")

#Chamando as funções def.
mostrar_imoveis()
escolher_imovel()