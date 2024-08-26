from xml.dom.minidom import parse

dom = parse("Parcers/imobiliaria.xml")

# Elemento raiz do XML (biblioteca)
biblioteca = dom.documentElement

# Recebe uma lista dos elementos com tag "imovel"
imoveis = biblioteca.getElementsByTagName('imovel')

# Acessa as informações de cada imovel
for imovel in imoveis:
    id = imovel.getAttribute('id')

    elemento_descricao = imovel.getElementsByTagName('descricao')[0]
    descricao = elemento_descricao.firstChild.nodeValue

    elemento_proprietario = imovel.getElementsByTagName('proprietario')[0]
    #Pega nome do proprietario
    nome_elements = elemento_proprietario.getElementsByTagName('nome')
    nome = nome_elements[0].firstChild.nodeValue if nome_elements else 'N/A'

    #Pega nome do email
    email_elements = elemento_proprietario.getElementsByTagName('email')
    email = email_elements[0].firstChild.nodeValue if email_elements else 'N/A'

    #Pega telefone do proprietario
    telefone_elements = elemento_proprietario.getElementsByTagName('telefone')
    telefones = [telefone.firstChild.nodeValue for telefone in telefone_elements]

    telefone1 = telefones[0] if len(telefones) > 0 else 'N/A'

    telefone2 = telefones[1] if len(telefones) > 1 else 'N/A'



    print("ID:", id)
    print("Descrição:", descricao)
    print(f'proprietario: {nome}')
    print(f'Email: {email}')
    print(f'Telefone:\n {telefone1} \n {telefone2}')
    print("---\n")