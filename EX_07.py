def volume_cilindro(r, a):
    volumen = 3.1416 * (r**2) * a
    return volumen

r = int(input("Digite o valor de raio: "))
a = int(input("Digite o valor de altura: "))
print(volume_cilindro(r , a))