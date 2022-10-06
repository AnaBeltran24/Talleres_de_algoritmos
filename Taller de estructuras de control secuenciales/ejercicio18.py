#entradas
bpr=int(input("ingrese la cantidad de bolivares que se prestaron"))
bpa=int(input("ingrese la cantidad de bolivares que se pagaron de interes en 4 años"))
#caja negra
razon=(bpa*100)/(bpr*4)
#salidas
print("el porcentaje que se cobró por el prestamo fue:", razon)