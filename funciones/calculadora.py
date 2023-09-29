#CALCULADORA
def sumna(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1,num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        resultado = num1 / num2
    except  Exception as e:
        resultado = None
    return resultado
    
def menu():
    while True:
        try:
            print("*** MENU CALCULADORA ***")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Divifir")
            print("5. Salir")
            op = int(input(">>> OPcion (1-5)? "))
            if op < 1 or op > 5:
                print("Opcion no valida. Esoja del 1 al 5.")
                continue
            return op
        except ValueError:
            print("Error. Opcion no valida.")
            input("Presione cualquier tecla para continuar")

##PROGRAMA PRINCIPAL
def leerNum():
    pass
while True:
    opcion = menu()
    if opcion == 1:
        num1 = leerNum("INgrese el primer numero")
        num2 = leerNum("INgrese el segundo numero")
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        print("\n\nGracias por usar la calculadora")
        print("Adios")
        input()





