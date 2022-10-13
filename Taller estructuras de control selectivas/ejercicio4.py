#entradas
x=int(input("ingrese el monto total de la compra:"))
#caja negra
if x>5000000:
    a=x*0.55 
    b=x*0.30  
    c=x*0.15
    d=c*0.20
#salidas
    print("la empresa invierte una cantidad de:",a )
    print("la empresa pidio prestado al banco una cantidad de:",b )
    print("la empresa solicito un credito al fabricante de:",c )
    print("el monto a pagar por los intereses es de:", d)
else:
    a=x*0.70
    b=x*0.30
    d=b*0.20
    print("la empresa invierte una cantidad de:",a)
    print("la empresa solicita un credito al fabricante de:",b)
    print("el monto a pagar por los intereses es de:", d)