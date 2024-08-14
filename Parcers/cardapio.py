from xml.dom.minidom import parse

dom = parse("Parcers/cardapio.xml")

# Elemento raiz do XML (cardapio.xml)
cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "prato"
pratos = cardapio.getElementsByTagName('prato')

# Mostrar pratos
for List_Prato in pratos:
    List_Prato_ID = List_Prato.getAttribute('id')

    elemento_list_nome = List_Prato.getElementsByTagName('nome')[0]
    list_nome = elemento_list_nome.firstChild.nodeValue
    
    elemento_list_descricao = List_Prato.getElementsByTagName('descricao')[0]
    list_descricao = elemento_list_descricao.firstChild.nodeValue

    elemento_ingredientes = List_Prato.getElementsByTagName('igredientes')[0]
    ingrediente_texto = elemento_ingredientes.getElementsByTagName('igrediente')[0].firstChild.nodeValue
        
    elemento_list_preco = List_Prato.getElementsByTagName('preco')[0]
    list_preco = elemento_list_preco.firstChild.nodeValue

    elemento_list_calorias = List_Prato.getElementsByTagName('calorias')[0]
    list_calorias = elemento_list_calorias.firstChild.nodeValue

    elemento_list_tempo = List_Prato.getElementsByTagName('tempo')[0]
    list_tempo = elemento_list_tempo.firstChild.nodeValue

    print(f"Prato ID: {List_Prato_ID} - {list_nome}")
    
# Para o usuario digitar o ID do prato
pratoID = input("Digite o ID do prato para mais informações: ")

# Para iniciar uma flag e verificar as informações do prato
prato_encontrado = False

# Acessa as informações de cada prato
for prato in pratos:
    idprato = prato.getAttribute('id')

    if idprato == pratoID:

        elemento_nome = prato.getElementsByTagName('nome')[0]
        nome = elemento_nome.firstChild.nodeValue
        
        elemento_descricao = prato.getElementsByTagName('descricao')[0]
        descricao = elemento_descricao.firstChild.nodeValue

        elemento_ingredientes = prato.getElementsByTagName('igredientes')[0]
        ingrediente_texto = elemento_ingredientes.getElementsByTagName('igrediente')[0].firstChild.nodeValue
        
        elemento_preco = prato.getElementsByTagName('preco')[0]
        preco = elemento_preco.firstChild.nodeValue

        elemento_calorias = prato.getElementsByTagName('calorias')[0]
        calorias = elemento_calorias.firstChild.nodeValue

        elemento_tempo = prato.getElementsByTagName('tempo')[0]
        tempo = elemento_tempo.firstChild.nodeValue

        print("Prato ID: ", idprato)
        print("Nome:", nome)
        print("Descrição:", descricao)
        print("Igredinentes: ", ingrediente_texto, ".")
        print("Preço: ", preco)
        print("Calorias: ", calorias)
        print("Tempo: ", tempo)
        print("-----------\n")

        prato_encontrado = True

        break

# Se a flag "prato_encontrado" ainda for igual a falso
if not prato_encontrado: # ou if prato_encontrado == False
    print("ID do prato não encontrado.")