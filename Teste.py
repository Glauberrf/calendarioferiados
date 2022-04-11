import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



userdata = {"tabela": "feriados_tb","data_registro": "06-04-2022", "data_feriado": "25/04/2022", "tipo": "Municipal / Nacional", "cidade": "Cajamar", "motivo": "Test de inserção de dados"}
resp = requests.post('http://loteria.eu5.org/feriados/insertferiado.php', params=userdata)

print(resp)


url = "http://loteria.eu5.org/feriados/selectferiadoall.php"

r = requests.get(url,params={"tabela":"feriados_tb"})
#print(r.content)
# Create a BeautifulSoup object

for linha in json.loads(r.content):
    
    userid = linha['motivo']
    print(userid)
#print(r.content)