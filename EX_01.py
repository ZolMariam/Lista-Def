#numero a binario
def decimal_para_binario(n):
    restos = []
    while n >0:
        resto = n % 2
        restos.append(resto)
        n = n // 2
    restos.reverse()
    return "".join(map(str, restos))
    
n = int(input("Digite um numero: "))
print(decimal_para_binario(n))