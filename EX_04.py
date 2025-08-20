def distancia_pontos(x1 , y1 , x2 , y2):
    resta_1 = x2 - x1
    resta_2 = y2 - y1
    
    elevado_1 = resta_1 ** 2
    elevado_2 = resta_2 ** 2
    
    suma = elevado_1 + elevado_2
    
    raiz = suma ** 0.5
    
    return raiz

x1 = float(input("Digite 1er numero: "))
y1 = float(input("Digite 2do numero: "))
x2 = float(input("Digite 3er numero: "))
y2 = float(input("Digite 4to numero: "))

print(distancia_pontos(x1 , y1 , x2 , y2))