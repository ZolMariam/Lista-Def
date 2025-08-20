#numero a binario
def decimal_para_binario(n):
    if n == 0:
        return "0"
    
    restos = []
    
    while n >0:
        resto = n % 2
        restos.append(str(resto))
        n = n // 2
    restos.reverse()
    return "".join(restos)
    
n = int(input("Digite um numero: "))
print(decimal_para_binario(n))