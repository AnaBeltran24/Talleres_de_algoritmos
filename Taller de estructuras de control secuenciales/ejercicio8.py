import math
#Entradas
ladou=float(input("Ingrese lado 1: "))
ladod=float(input("Ingrese lado 2: "))
ladot=float(input("Ingrese lado 3: "))
#Caja negra
s= (ladou+ladod+ladot)/2
area= math.sqrt(s*(s-ladou)*(s-ladod)*(s-ladot))
#salida
print("El area es: "+str(area))