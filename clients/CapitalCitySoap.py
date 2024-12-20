import requests
from xml.dom.minidom import parseString

# Função para enviar a requisição e processar a resposta com xml.dom.minidom
def send_request_and_parse(payload, tag_name):
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
    headers = {'Content-Type': 'text/xml; charset=utf-8'}
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # Analisar a resposta XML
    dom = parseString(response.text)
    elements = dom.getElementsByTagName(tag_name)
    
    # Extrair e exibir os valores
    if elements:
        for element in elements:
            print(f"{tag_name}: {element.firstChild.nodeValue}")
    else:
        print(f"Tag {tag_name} não encontrada na resposta.")

# 1: Nome da Capital do País (NZ)
print("\n1: Nome da Capital do País (NZ):")
payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>NZ</sCountryISOCode>
        </CapitalCity>
    </soap:Body>
</soap:Envelope>"""
send_request_and_parse(payload, "m:CapitalCityResult")

# 2: Nome do País (NZ)
print("\n2: Nome do País (NZ):")
payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>NZ</sCountryISOCode>
        </CountryName>
    </soap:Body>
</soap:Envelope>"""
send_request_and_parse(payload, "m:CountryNameResult")

# 3: Código de Telefone (BR)
print("\n3: Código de Telefone (BR):")
payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <CountryIntPhoneCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>BR</sCountryISOCode>
        </CountryIntPhoneCode>
    </soap:Body>
</soap:Envelope>"""
send_request_and_parse(payload, "m:CountryIntPhoneCodeResult")

# 4: Nome da Moeda (BR)
print("\n4: Nome da Moeda (BR):")
payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <CurrencyName xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCurrencyISOCode>BRL</sCurrencyISOCode>
        </CurrencyName>
    </soap:Body>
</soap:Envelope>"""
send_request_and_parse(payload, "m:CurrencyNameResult")
