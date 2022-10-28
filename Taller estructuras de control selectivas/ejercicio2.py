#entradas
x=int(input("Digite el sueldo del trabajador"))
#caja negra 
if x<900000:
    y=x+(x*0.15)
else: 
    y=x+(x*0.12)
#salidas
print("el nuevo sueldo del trabajador es de:", y)