def binario_para_decimal(binario):
    if not all(c in "01" for c in binario):
        return ""
    
    decimal = 0
    long = len(binario)
    
    for i in range(long):
        bit = int(binario[i])
        potencia = long - 1 - i
        decimal += bit * (2 ** potencia)
        
    return decimal
    
binario = input("Digite o numero: ")
print(binario_para_decimal(binario))