def raio_circulo(area):
    raio = area / 3.1416
    
    raiz = raio ** 0.5
    
    return raiz

area = float(input("Digite un numero: "))
print(raio_circulo(area))