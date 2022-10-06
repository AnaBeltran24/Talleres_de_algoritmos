#entradas
mujeres=int(input("ingrese la cantidad de mujeres: "))
hombres=int(input("ingrese la cantidad de hombres: "))
#caja negra
Total=mujeres+hombres
M=round((mujeres*100)/Total)
H=round((hombres*100)/Total)
#salidas
print("El porcentaje de mujeres es:", M)
print("El porcentaje de hombres es:", H)