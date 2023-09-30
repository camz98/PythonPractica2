def encontrar_factorial(numero=5):
    if numero < 0:
        return "El factorial no está definido para números negativos"
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

resultado = encontrar_factorial(numero=5)
print(f"El factorial de 5 es {resultado}")