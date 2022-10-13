#entradas
T=int(input("ingrese la temperatura en farenheit "))
#caja negra y salidas
if T>85:
    print("el deporte apropiado para practicar es natación")
if 70<T<=85:
    print("el deporte apropiado para practicar es tenis")
if 32<T<=70:
    print("el deporte apropiado para practicar es golf")
if 10<T<=32:
    print("el deporte apropiado para practicar es esqui")
if T<=10:
    print("el deporte apropiado para practicar es marcha")