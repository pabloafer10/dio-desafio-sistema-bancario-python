# Menu de opções de operações bancárias
menu = """

[0]   Depositar
[1]   Sacar
[2]   Extrato
[3]   Sair

=> """

# Variáveis de controle do desafio
saldo = 0
limitesaque = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

# Laço de repetição para exibir o menu de opções
while True:

    opcao = input(menu)

    # Depositos somente em valores positivos, todos dpósitos deves ser armazenados em uma variavel e exibir na operação de extrato
    if opcao == '0': 
            valor = float(input("Digite o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"     
            else:
                 print("Valor inválido, tente novamente.")
    
    # Saques com limite diario de 3 e com valor máximo de R$ 500,00 por saque, todos dpósitos deves ser armazenados em uma variavel e exibir na operação de extrato. Saque maior que limite deve exibir mensagem informando que não foi possível realizar operação por saldo insuficiente, todos saques deves ser armazenados em uma variavel e exibir na operação de extrato
    elif opcao == '1':
            valor = float(input("Digite o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limitesaque
            excedeu_saques = numero_saque >= LIMITE_SAQUE
            
            if excedeu_saldo:
                print("Saldo insuficiente! Por favor, tente novamente.")
            elif excedeu_limite:
                 print("Valor de saque maior que o limite! Por favor, tente novamente.")
            elif excedeu_saques:
                print("Limite de saques diário excedido,! Por favor, tente novamente.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1

            else:
                print("Valor informado inválido, tente novamente.")

    # Extrato deve listar todos os depósitos e saques realizado. No final deverá exibir saldo disponível em conta com formato R$ xxx.xx
    elif opcao == '2':  
            print("\n-----------------  Extrato  -----------------")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo disponível: R$ {saldo:.2f}")
            print("---------------------------------------------\n")

    # Em caso de desejar sair informar opção.
    elif opcao == '3':
        break   

    # Em caso de input for != da liste de menu, devera exibir mensagem de opção inválida e solicitar novamente a operação desejada.
    else:
        print("Opção inválida, por favor seleciona novamente a operação desejada.")

