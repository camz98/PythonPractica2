datos={'alumno':'alumn',
       'nota1':'not1',
       'nota2':'not2',
       'nota3':'not3',}
while True:
  numero=input("desea ingresar un registro? : ")
  if numero=="si": 
    alumn=input("Nombre del alumno: ")
    not1=input("Primera nota del alumno: ")
    not2=input("Segunda nota del alumno: ")
    not3=input("tercera nota del alumno: ")
    datos['alumno']=alumn
    datos['nota1']=not1
    datos['nota2']=not2
    datos['nota3']=not3          
  elif numero=="no":
      break
for i in  datos:
 print(datos)
 
