N=int(input("ingrese la cantidad de estudiantes "))
i=int(0)
lista=[]
while i<N:
    i+=1
    ab=input("ingrese su nombre y su puntaje ")
    a,b=ab.split()
    a=str(a)
    b=int(b)
    lista.append(b)
r=max(lista)
y=min(lista)
if b==r:
    nombre=a
    print("el estudiante con la calificacion mas alta es:",nombre)
