dicEscuela = {}
bandera = True
while True:
    dicEstudiantes = {}
    if bandera == True:
        Codigo = int("Ingrese el codigo del estudiante: ")
        Nombre = input("Ingrese el nombre del estudiante: ")
        Note1 = float(input("Ingrese la nota 1 del estudiante [0 - 5.0]"))
        Note2 = float(input("Ingrese la nota 2 del estudiante [0 - 5.0]"))
        Note3 = float(input("Ingrese la nota 3 del estudiante [0 - 5.0]"))
        if Codigo == 999:
            bandera == False
    break

    

