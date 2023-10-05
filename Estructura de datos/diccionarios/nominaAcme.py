dicEmpresa = {}
dicEmpleado = {}

#AGREGAR EMPLEADO
def agregarEmpleado():
    id = int(input("Digite el ID del empelado (cedula): "))
    dicEmpleado["Nombre"] = input("Ingrese el nombre del empleado: ")
    dicEmpleado["horasTrabajadas"] = int(input("Ingrese cuantas horas trabajo [1h -> 160h]: "))
    dicEmpleado["valorHora"] = float(input("Digite el valor de la hora [8k -> 150k]: "))
    dicEmpresa[id] = dicEmpleado

def modificarEmpleado():
    pass

