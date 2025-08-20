import random
def gerar_numeros_aleatorios(n , m):
    numero = random.randint(n, m)
    
    return numero

n = int(input("Digite um numero: "))
m = int(input("Digite mais um numero: "))
print(gerar_numeros_aleatorios(n, m))