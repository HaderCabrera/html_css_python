dicEmpresa = {}

def agregarEmpleado():
    dicEmpleado = {}
    id = int(input("Digite el ID del empelado (cedula): "))
    dicEmpleado["Nombre"] = input("Ingrese el nombre del empleado: ")
    dicEmpleado["horasTrabajadas"] = int(input("Ingrese cuantas horas trabajo [1h -> 160h]: "))
    dicEmpleado["valorHora"] = float(input("Digite el valor de la hora [8k -> 150k]: "))
    dicEmpresa[id] = dicEmpleado

def modificarEmpleado():
    empleado = int(input("Digite el ID [CC] del empleado que desea modificar: "))
    print("====QUE DESEA MODIFICAR?==== ")
    print("     1. Nombre")
    print("     2. horasTrabajadas")
    print("     3. valorHora")
    op = int(input("Digite la opcion que desea modificar: "))
    if op == 1:
        dicEmpresa[empleado]["Nombre"] = input("    Ingrese el nuevo nombre >>> ")
    if op == 2:
        dicEmpresa[empleado]["horasTrabajadas"] = input("   Ingrese la nueva cantidad de horas >>> ")
    if op == 3:
        dicEmpresa[empleado]["valorHora"] = input("   Ingrese el nuevo valor de la hora >>> ")

def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado")
            print("2. Modificar empleado")
            print("3. Buscar emplado")
            print("4. Eliminar empleado")
            print("5. Listar empleados")
            print("6. Listar nómina de un empleado")
            print("7. Listar nómina de todos los empleados")
            print("8. Salir")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

while True:
    opcion = menu()
    if opcion == 1:
        agregarEmpleado()
        print(dicEmpresa)
    elif opcion == 2:
        modificarEmpleado()
        print(dicEmpresa)



