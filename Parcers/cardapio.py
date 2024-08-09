from xml.dom.minidom import parse

dom = parse("Parcers/cardapio.xml")

# Elemento raiz do XML (cardapio.xml)
cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "prato"
pratos = cardapio.getElementsByTagName('prato')

# Acessa as informações de cada prato
for prato in pratos:
    idprato = prato.getAttribute('id')

    elemento_nome = prato.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    
    elemento_descricao = prato.getElementsByTagName('descricao')[0]
    descricao = elemento_descricao.firstChild.nodeValue

    elemento_preco = prato.getElementsByTagName('preco')[0]
    preco = elemento_preco.firstChild.nodeValue

    elemento_calorias = prato.getElementsByTagName('calorias')[0]
    calorias = elemento_calorias.firstChild.nodeValue

    elemento_tempo = prato.getElementsByTagName('tempo')[0]
    tempo = elemento_tempo.firstChild.nodeValue

    print("Prato :", idprato)
    print("Nome:", nome)
    print("Descrição:", descricao)
    print("Preço: ", preco)
    print("Calorias: ", calorias)
    print("Tempo: ", tempo)
    print("-----------\n")