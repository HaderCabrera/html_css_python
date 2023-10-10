import random
listJugadores = []
def leerNombre(msj):
    while True:
        try:
            nombre = input(msj)
            nombre = nombre.strip()
            if len(nombre) == 0 or not nombre.isalnum():
                print("Nombre inválido")
                continue
            return nombre
        except Exception as e:
            print("Error al ingresar el nombre.", e)
def leerInt(msj):
    while True:
        try:
            id = int(input(msj))
            if id < 0:
                print("Ingrese un número positivo mayor a cero...")
                continue
            return id
        except ValueError:
            print("Error. Número invalido. ingrese número correcto")
def jugar(player):
    dictPlayer = {}
    numero = random.randint(1,20)
    bandera = 1
    
    for i in range(10):
        intento = leerInt("Adivine el numero>>>  ")
        if i == 9 and numero != intento:
            dictPlayer[player] = "No lo lograste"
            listJugadores.append(dictPlayer)
        elif intento > numero:
            print("Digite un numero MENOR. ")
        elif intento < numero:
            print("Digite un numero MAYOR.")
        elif intento == numero:
            print("EXITO, HAS ADIVINADO.")
            dictPlayer[player] = bandera
            listJugadores.append(dictPlayer)
            break
        bandera += 1

def sacarTop():
    pass

while True:
    nombre = leerNombre("\nIngrese el nombre del PLAYER:   ")
    jugar(nombre)
    print(listJugadores)
    a = input("DESEA SEGUIR JUGANDO? ")
    if a == "S" or a == "s":
        continue
    else:
        break

