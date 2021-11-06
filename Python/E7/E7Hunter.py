# 'Daniel Ernesto Rangel Perez
# 'Sergio Javier Juárez Torres
# 'Dariela Hurtado Torres
# 'Jesús Alexandro Cervantes
from pyhunter import PyHunter
from openpyxl import Workbook
import getpass


def Busqueda(organizacion):
    # 'Cantidad de resultados esperados de la búsqueda
    # 'El límite MENSUAL de Hunter es 50, cuidado!
    resultado = hunter.domain_search(company=organizacion, limit=1,
                                     emails_type='personal')
    return resultado


def GuardarInformacion(datosEncontrados, organizacion):
    libro = Workbook()
    hoja = libro.active
    hoja["A1"] = "Dominio"
    hoja["B1"] = "Organizacion"
    hoja["C1"] = "Pais"
    hoja["D1"] = "Email"
    hoja["E1"] = "Tipo de Email"
    hoja["F1"] = "Nombre"
    hoja["G1"] = "Apellido"
    # 'Guardar datos
    hoja["A2"] = datosEncontrados['domain']
    hoja["B2"] = datosEncontrados['organization']
    hoja["C2"] = datosEncontrados['country']

    # 'Guardar Emails ya que es otro diccionario
    Email = datosEncontrados['emails']
    diccionarioEmail = Email[0]
    hoja["D2"] = diccionarioEmail["value"]
    hoja["E2"] = diccionarioEmail["type"]
    hoja["F2"] = diccionarioEmail['first_name']
    hoja["G2"] = diccionarioEmail['last_name']
    libro.save("Hunter"+organizacion+".xlsx")

print("Script para buscar información")
apikey = getpass.getpass("Ingresa tu API key: ")
hunter = PyHunter(apikey)
orga = input("Dominio a investigar: ")
datosEncontrados = Busqueda(orga)
if datosEncontrados is None:
    exit()
else:
    print(datosEncontrados)
    print(type(datosEncontrados))
    GuardarInformacion(datosEncontrados, orga)
