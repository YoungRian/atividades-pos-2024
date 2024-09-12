from xml.dom.minidom import parse
import json

def parse_imovel(imovel):
    #Pega o id do imovel
    id = imovel.getAttribute('id')

    #Pega descrição
    elemento_descricao = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue.strip() if imovel.getElementsByTagName('descricao') else 'N/A'

    #Pega proprietário
    elemento_proprietario = imovel.getElementsByTagName('proprietario')[0]
    #Pega nome do proprietário
    nome = (elemento_proprietario.getElementsByTagName('nome')[0].firstChild.nodeValue.strip() 
        if elemento_proprietario.getElementsByTagName('nome') and elemento_proprietario.getElementsByTagName('nome')[0].firstChild else 'N/A')
    #Pega email do proprietário
    email = (elemento_proprietario.getElementsByTagName('email')[0].firstChild.nodeValue.strip() 
        if elemento_proprietario.getElementsByTagName('email') and elemento_proprietario.getElementsByTagName('email')[0].firstChild else 'N/A')
    #Pega telefone do proprietário
    telefones = [telefone.firstChild.nodeValue.strip() 
        for telefone in elemento_proprietario.getElementsByTagName('telefone') 
        if telefone.firstChild]
    telefone1 = telefones[0] if len(telefones) > 0 else 'N/A'
    telefone2 = telefones[1] if len(telefones) > 1 else 'N/A'

    #Pega endereço
    elemento_endereco = imovel.getElementsByTagName('endereco')[0]
    rua = (elemento_endereco.getElementsByTagName('rua')[0].firstChild.nodeValue.strip() 
        if elemento_endereco.getElementsByTagName('rua') and elemento_endereco.getElementsByTagName('rua')[0].firstChild else 'N/A')
    #Pega bairro
    bairro = (elemento_endereco.getElementsByTagName('bairro')[0].firstChild.nodeValue.strip() 
        if elemento_endereco.getElementsByTagName('bairro') and elemento_endereco.getElementsByTagName('bairro')[0].firstChild else 'N/A')
    #Pega nome da Cidade
    cidade = (elemento_endereco.getElementsByTagName('cidade')[0].firstChild.nodeValue.strip() 
        if elemento_endereco.getElementsByTagName('cidade') and elemento_endereco.getElementsByTagName('cidade')[0].firstChild else 'N/A')
    #Pega numero do imovel
    numero = (elemento_endereco.getElementsByTagName('numero')[0].firstChild.nodeValue.strip() 
        if elemento_endereco.getElementsByTagName('numero') and elemento_endereco.getElementsByTagName('numero')[0].firstChild else 'N/A')
    
    #Pega características
    elemento_caracteristicas = imovel.getElementsByTagName('caracteristicas')[0]
    tamanho = (elemento_caracteristicas.getElementsByTagName('tamanho')[0].firstChild.nodeValue.strip() 
        if elemento_caracteristicas.getElementsByTagName('tamanho') and elemento_caracteristicas.getElementsByTagName('tamanho')[0].firstChild else 'N/A')
    #Pega numero de quartos
    numQuartos = (elemento_caracteristicas.getElementsByTagName('numQuartos')[0].firstChild.nodeValue.strip() 
        if elemento_caracteristicas.getElementsByTagName('numQuartos') and elemento_caracteristicas.getElementsByTagName('numQuartos')[0].firstChild else 'N/A')
    #Pega numero de banheiros
    numBanheiros = (elemento_caracteristicas.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue.strip() 
        if elemento_caracteristicas.getElementsByTagName('numBanheiros') and elemento_caracteristicas.getElementsByTagName('numBanheiros')[0].firstChild else 'N/A')

    #Pega valor
    elemento_valor = (imovel.getElementsByTagName('valor')[0].firstChild.nodeValue.strip() 
        if imovel.getElementsByTagName('valor') and imovel.getElementsByTagName('valor')[0].firstChild else 'N/A')

    return {
        "id": id,
        "descricao": elemento_descricao,
        "proprietario": {
            "nome": nome,
            "email": email,
            "telefones": [telefone1, telefone2]
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numero de quartos": numQuartos,
            "numero de banheiros": numBanheiros,
        },
        "valor": elemento_valor
    }

def main():
    dom = parse("Parcers/imobiliaria.xml")
    biblioteca = dom.documentElement
    imoveis = biblioteca.getElementsByTagName('imovel')
    
    lista_imoveis = [parse_imovel(imovel) for imovel in imoveis]

    with open("json/imobiliaria2.json", "w", encoding='utf-8') as file:
        json.dump(lista_imoveis, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
