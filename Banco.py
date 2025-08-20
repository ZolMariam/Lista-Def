def simular_banco():
    contas = {} 

    while True:
        print("\n--- MENU BANCO ---")
        print("1. Criar nova conta")
        print("2. Depositar dinheiro")
        print("3. Sacar dinheiro")
        print("4. Exibir saldo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # criar conta
            nome = input("Digite o nome do titular: ")
            if nome in contas:
                print("Conta já existe!")
            else:
                saldo = float(input("Digite o saldo inicial: "))
                contas[nome] = saldo
                print(f"Conta de {nome} criada com saldo {saldo:.2f}")

        elif opcao == "2":  # depositar
            nome = input("Nome da conta: ")
            if nome not in contas:
                print("Conta não encontrada!")
            else:
                valor = float(input("Valor do depósito: "))
                contas[nome] += valor
                print(f"Depósito de {valor:.2f} realizado na conta de {nome}")

        elif opcao == "3":  # sacar
            nome = input("Nome da conta: ")
            if nome not in contas:
                print("Conta não encontrada!")
            else:
                valor = float(input("Valor do saque: "))
                if valor > contas[nome]:
                    print("Saldo insuficiente!")
                else:
                    contas[nome] -= valor
                    print(f"Saque de {valor:.2f} realizado na conta de {nome}")

        elif opcao == "4":
            nome = input("Nome da conta: ")
            if nome not in contas:
                print("Conta não encontrada!")
            else:
                print(f"Saldo da conta de {nome}: {contas[nome]:.2f}")

        elif opcao == "5":  # sair
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")
