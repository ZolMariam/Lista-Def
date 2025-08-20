def area_circulo(raio):
    area = 3.14 * (raio **2)
    
    return area

raio = int(input("Digite o raio do circulo: "))
print(area_circulo(raio))
