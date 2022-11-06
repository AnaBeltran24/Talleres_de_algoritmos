a=input()
(a1,a2,a3,a4)=a.split(" ")
a1=int(a1)
a2=int(a2)
a3=int(a3)
a4=int(a4)
x=a4
s=a1+a2+a3+a4
r=a2-a1
r=a4-a3
for n in range(1,9):
    if (n<9):
        x+=r
        s+=x
        if (n==9):
            break

print("a12:", x)
print("la suma de los 12 primeros terminos es:", s)