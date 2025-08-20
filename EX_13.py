def eh_par(par):
    resto = par % 2
    
    if resto == 0:
        return True
    else:
        return False
    
par = int(input("Digite o numero: "))
print(eh_par(par))