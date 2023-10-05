empleado = {"nombre": "Hader Cabrera" , "Cargo": "Programador","Salario": 4000000}
#OBTENER DATO DENTRO DEL DICCIONARIO
print(empleado["Cargo"])
print(empleado.get("Cargo"))

#PONER MENSAJE CUANDO NO EXISTE LLAVE
print(empleado.get("Apellido","NO EXITE")) #DEVUELVE NONE POR DEFECTO
#print(empleado("Apellido")) #DEVUELVE ERROR

#AGREGAR LLAVE A DICCIONARIO
empleado["sexo"] = "Masculino"
print(empleado)

#MoODIFICAR SALAROIO
empleado["Salario"] = 4500000
print(empleado)

#BORRAR LLAVE CON SU VALOR
del empleado["sexo"]
print(empleado)

#BORRAR TODO EL DICCIONARIO
#empleado = {}
#empleado.clear()
#del empleado #LA FUNCION DEL BORRA VARIABLE

#COPIAR DICCIONARIO SIN MODIFICAR EL INICIAL
oficina = empleado.copy()
print(oficina)
oficina["salario"] = 5000000
print(oficina)
print(empleado)
