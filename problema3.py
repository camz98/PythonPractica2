variables=[]

while True:    
    numero=input("desea ingresar un numero? : ")
    if numero=="si": 
      valor=int(input("ingresa el numero: "))
      for i in range(1):        
        variables.append(valor)      
    elif numero=="no":
      break
print(f"Los numeros ingresados son: {variables}")
