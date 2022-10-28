#entradas
A=int(input("valor de A:"))
B=int(input("valor de B:"))
C=int(input("valor de C:"))
D=int(input("valor de D:"))
#caja negra
if D==0:
    x=(A-C)**2
if D>0:
    x=((A-B)**3)/D
#salidas
print(x)