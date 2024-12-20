import requests
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# XML estruturado

# 1: Nome da Capital do Pais (NZ)
payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>NZ</sCountryISOCode>
        </CapitalCity>
    </soap:Body>
</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)
print("\n4. Resposta - Capital do País (NZ):")
print(response.text)
