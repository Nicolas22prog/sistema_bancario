menu = '''
    ########## Menu ##########
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair
    ##########################
    
'''


saldo = 0 
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito: ")
        valor = float(input("Valor do deposito: "))
        if valor < 0:
            print("Valor inválido")
            print(opcao)
            saldo -= valor
        saldo += valor
        extrato += f"Deposito : R$ {valor:.2f}\n"
       


    elif opcao == "s":
        print("Saque: ")
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Valor do saque: "))
            if valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
        else:
            print("Não foi possivel realizar o saque, Verifique o saldo e o limite da conta!")



    
    elif opcao == "e":
        print("Extrato".center(28,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("".center(28,"="))
        print("Saldo")
        print(f"{saldo:.2f}")
    
    elif opcao == "q":
        print("Obrigado e volte sempre!")
        break
else:
    print("Opção Invalida!")
