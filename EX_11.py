def hipotenusa(cat1 , cat2):
    cat1_elev = cat1 ** 2
    cat2_elev = cat2 ** 2
    
    suma = cat1_elev + cat2_elev
    
    raiz = suma**0.5
    
    return raiz

cat1 = float(input("Digite o valor do primer cateto: "))
cat2 = float(input("Digite o valor do segundo cateto: "))
print(hipotenusa(cat1 , cat2))