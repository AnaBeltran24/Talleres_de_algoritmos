usuarios ={
    "iperurena":{
        "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    },
}
for i in range(1,4,1):
    U= input("Usuario:")
    C= input("Contraseña:")
    if U in usuarios and C==usuarios[U]["password"]:
        a=usuarios[U]["nombre"]
        b=usuarios[U]["apellido"]
        print(a)
        print(b)
        break
    if i==3:
        print("No tiene mas intentos")
        break
    else:
        print("Intentelo de nuevo")