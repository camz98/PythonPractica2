def encontrar_numero(numero=20):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"
resultado=encontrar_numero(numero=20)   
print(resultado)