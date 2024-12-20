import zeep

# define a URL do WSDL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o código do país para BR
country_code = "NO"

# faz a chamada do serviço
result = client.service.CapitalCity(
	sCountryISOCode=country_code
)
# imprime o resultado
print(f"A capital do país {country_code} é {result}")