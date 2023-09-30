def cantidad_numero(a,b):
 c=0
 while a>0:
    if b==a%10:
       c+=1
    a=a//10
 return c
a=int(input("ingresa un numero:"))
b=int(input("ingresa un digito: "))
print(cantidad_numero(a,b)) 
