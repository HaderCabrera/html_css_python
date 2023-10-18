
import json
rutaFile = "hader_cabrera/talleres/datpersonal.json"
lista = ["hola","como","esta"]
while True:
    try:
        fd = open(rutaFile, "r")
        print("Entre a lectura")
    except Exception as e:
        try:
            fd = open(rutaFile, "w")
            print("entre a escributra")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            break
"""  try:
    json.dump("hola",fd)
except Exception as e:
    print("Error al cargar la información\n", e)
    input("Presione cualquier tecla para continuar\n")
    break

# print(lstPersonal)
try:
    if not fd.closed:
        fd.close()
except Exception as e:
    print("Error al cerrar el archivo.\n", e, "\n")
    input("Presione cualquier tecla para continuar\n")
    break
"""