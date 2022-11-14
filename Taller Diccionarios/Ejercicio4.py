x=int(input("Cantidad de estudiantes: "))
lista_a=[]
lista_s=[]
notas=[]
estudiantes={}

for c in range(1,x+1,1):
    ne=input("Nombre del estudiante:")
    nt=float(input("Nota del estudiante:"))
    estudiantes.update({c:{"nombre":ne, "nota":nt}})

for i in estudiantes.keys():
    if (estudiantes[i]["nota"])<=5:
            lista_s.append(estudiantes[i]["nombre"])
    if (estudiantes[i]["nota"])>5:
        lista_a.append(estudiantes[i]["nombre"])
    notas.append(estudiantes[i]["nota"])

media=(sum(notas))/x

print("Estudiantes suspendidos:",lista_s)
print("Estudiantes aprobados:",lista_a)
print("Nota media de la clase:",media)