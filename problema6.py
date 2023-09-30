def numero_fibonacci(n):
    a=0
    b=1

    for i in range(n):
        c=a+b
        a=b
        b=c
    return b
for j in range(10):
 print(numero_fibonacci(j))