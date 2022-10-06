#entradas
ck=int(input("ingrese el costo por kilovatio "))
lectura_anterior=int(input("ingrese la lectura anterior en kilovatios"))
lectura_actual=int(input("ingrese la lectura actual en kilovatios"))
#caja negra
T=(lectura_actual-lectura_anterior)/ck
#salidas
print("el monto total a pagar es de:",T)