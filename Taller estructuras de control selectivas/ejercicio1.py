#entradas
A=int(input("ingrese la cantidad de dinero invertido en el banco"))
B=int(input("ingrese el porcentaje que paga el banco por interes al mes"))
#caja negra y salidas
C=(A*(B/100))/12
D=A+C
if C>100000:
    print("La cantidad de dinero en la cuenta es de:", D)
else:
    print("la cantidad de dinero en la cuenta es de:", A)