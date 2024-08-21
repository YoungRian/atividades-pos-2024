import xmltodict

import json

xml_imobiliaria = """<?xml version="1.0" encoding="utf-8"?>

<imobiliaria>
    <imovel id="A1">
        <descricao>Apartamento grande</descricao>
        <proprietario>
            <nome>Joedson</nome>
            <email>joedson.rian@gmail.com</email>
            <telefone>84 999650665</telefone>
            <telefone>84 123456789</telefone>
        </proprietario>
        <endereco>
            <rua>Rua YK</rua>
            <bairro>Manhattan</bairro>
            <cidade>Nova York</cidade>
            <numero>507</numero>
        </endereco>
        <caracteristicas>
            <tamanho>250m²</tamanho>
            <numQuartos>20</numQuartos>
            <numBanheiros>40</numBanheiros>
        </caracteristicas>
        <valor>125,000,000</valor>
    </imovel>

    <imovel id="A2">
        <descricao>Casa de primeiro andar</descricao>
        <proprietario>
            <nome>Simão</nome>
            <email>simao.pedro@gmail.com</email>
            <telefone>84 40028922</telefone>
        </proprietario>
        <endereco>
            <rua>Rua Vinte e Cinco de Abril</rua>
            <bairro>Espirito Santo</bairro>
            <cidade>Carburador</cidade>
            <numero></numero>
        </endereco>
        <caracteristicas>
            <tamanho>50m²</tamanho>
            <numQuartos>6</numQuartos>
            <numBanheiros>5</numBanheiros>
        </caracteristicas>
        <valor>80,000</valor>
    </imovel>
</imobiliaria>"""

imobiliaria_dict = xmltodict.parse(xml_imobiliaria)

json_imobiliaria = json.dumps(imobiliaria_dict, indent=4, ensure_ascii=False)

print(json_imobiliaria)