import random
def jogar_adivinhacao():
    goal = random.randint(1 , 100)
    min = 1
    max = 100
    
    total_intentos = 10
    for intentos in range(1, total_intentos + 1):
        restante = total_intentos - intentos
        try: 
            intento = int(input(f"Chuta de {min} a {max}! Tem {restante} intentos! "))
        except ValueError:
            print("Valor invalido. tente novamente.")
            continue
                
        if intento == goal:
            print("Parabens!! Acertou!")
            return
        
        elif intento > goal:           
            print(f"O numero é menor.") 
            max = intento - 1
                   
        elif intento < goal:
            print(f"O numero é maior.")
            min = intento + 1
        
print(jogar_adivinhacao())