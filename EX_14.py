def eh_impar(impar):
    resto = impar % 2
    if resto != 0:
        return True
    else:
        return False 

impar = int(input("Digite seu numero: "))
print(eh_impar(impar))