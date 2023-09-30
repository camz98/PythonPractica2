def cadena_texto(texto):
    texto_sin_vocales = texto.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')    
    return texto_sin_vocales
texto = input("Ingresa una cadena de texto: ")

resultado = cadena_texto(texto)

print(f"Texto sin vocales:{resultado}")