def numero_digitos(n):
    contador = 0
    while n > 0:
        n //= 10
        contador += 1
        
    return contador
        
n = int(input("Digite seu numero: "))
print(numero_digitos(n))