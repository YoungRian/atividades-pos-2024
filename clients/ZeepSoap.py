import zeep

# define a URL do WSDL
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o numero escolhido 
numero_escolhido = "2012"

# faz a chamada do serviço
result = client.service.NumberToWords(
	ubiNum = numero_escolhido
)
# imprime o resultado
print(f"{result}")