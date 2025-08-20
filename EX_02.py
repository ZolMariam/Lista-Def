def calcular_imc(peso , altura):
    imc = peso / (altura ** 2)
    
    return imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura (Ex. 1.60): "))

print(calcular_imc(peso, altura))