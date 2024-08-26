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

    #pega proprietario
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

    #\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////

    #Pega endereço
    elemento_endereco = imovel.getElementsByTagName('endereco')[0]

    #Pega rua de endereco
    rua_elements = elemento_endereco.getElementsByTagName('rua')
    rua = rua_elements[0].firstChild.nodeValue if rua_elements else 'N/A'

    #Pega bairro de endereco
    bairro_elements = elemento_endereco.getElementsByTagName('bairro')
    bairro = bairro_elements[0].firstChild.nodeValue if bairro_elements else 'N/A'

    #Pega cidade de endereco
    cidade_elements = elemento_endereco.getElementsByTagName('cidade')
    cidade = cidade_elements[0].firstChild.nodeValue if cidade_elements else 'N/A'

    #Pega numero de endereco
    numero_elements = elemento_endereco.getElementsByTagName('numero') if elemento_endereco else []
    numero = numero_elements[0].firstChild.nodeValue.strip() if numero_elements and numero_elements[0].firstChild else 'N/A'
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////

    #Pega Caracteristicas
    elemento_caracteristicas = imovel.getElementsByTagName('caracteristicas')[0]

    #Pega tamahno de caracteristicas
    tamanho_elements = elemento_caracteristicas.getElementsByTagName('tamanho')
    tamanho = tamanho_elements[0].firstChild.nodeValue if tamanho_elements else 'N/A'

    #Pega numQuartos de caracteristicas
    numQuartos_elements = elemento_caracteristicas.getElementsByTagName('numQuartos')
    numQuartos = numQuartos_elements[0].firstChild.nodeValue if numQuartos_elements else 'N/A'

    #Pega numBanheiros de caracteristicas
    numBanheiros_elements = elemento_caracteristicas.getElementsByTagName('numBanheiros')
    numBanheiros = numBanheiros_elements[0].firstChild.nodeValue if numBanheiros_elements else 'N/A'

    #\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////

    #Pega Valor
    valor_elements = imovel.getElementsByTagName('valor')[0]
    valor = valor_elements.firstChild.nodeValue if valor_elements else 'N/A'

    print("ID:", id)
    print("Descrição: ", descricao)
    print(f'proprietario : {nome}')
    print(f'Email: {email}')
    print(f'Telefone:\n {telefone1} \n {telefone2}')
    print(f"Endereço: ")
    print("rua: ", rua)
    print("bairro: ", bairro)
    print("cidade: ", cidade)
    print("numero: ", numero)
    print("Valor: ", valor)
    print("---\n")
