Algoritmo distancias
	Escribir "Digite la distancia en la cual se situa el primer coche:"
	leer d1
	Escribir "Digite la distancia en la cual se situa el segundo coche:"
	Leer d2
	Escribir "Digite la velocidad del primer carro (mas lento):"
	leer v1
	Escribir "Digite la velocidad del segundo carro (mas rapido):"
	leer v2
	Diferenciav<-v2-v1
	tiempo<-(d1+d2)/(Diferenciav)
	Tiempo<-tiempo * 60
	Escribir "ambos vehiculos coincidiran una vez transcurridos" Tiempo "minutos"
	
FinAlgoritmo
