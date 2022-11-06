x=int(input("Cantidad de estudiantes:"))
lista=[]
y=0
while y<x:
    y=y+1
    a=float(input("Estatura:"))
    lista.append(float(a))
    if y==x:
        r=max(lista)
        print("La estatura mayor es:",r)