dicEscuela = {}
bandera = True
while bandera == True:
    dicEstudiantes = {}
    if bandera == True:
        codigo = int(input("Ingrese el codigo del estudiante: "))
        if codigo == 999:
            break
        else:
            dicEstudiantes["Nombre"] = input("Ingrese el nombre del estudiante: ")
            dicEstudiantes["Note1"] = float(input("Ingrese la nota 1 del estudiante [0 - 5.0]"))
            dicEstudiantes["Note2"] = float(input("Ingrese la nota 2 del estudiante [0 - 5.0]"))
            dicEstudiantes["Note3"] = float(input("Ingrese la nota 3 del estudiante [0 - 5.0]"))
        
        dicEscuela[codigo] = dicEstudiantes
print(dicEscuela)
    

