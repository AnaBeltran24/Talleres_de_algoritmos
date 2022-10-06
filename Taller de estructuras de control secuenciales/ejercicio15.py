#entradas
PVP=int(input("ingrese el precio del producto sin descuento"))
PVF=int(input("ingrese el precio pagado por el producto con el descuento"))
#caja negra
Desc=100-((PVF*100)/PVP)
#salidas
print("el porcentaje del descuento hecho al producto es de:", Desc)