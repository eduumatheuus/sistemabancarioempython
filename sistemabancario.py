menu = """
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print ("Depósito")
        valor = float(input("Digite qual valor você deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print ("Depositado com sucesso!")
        else:
            print("Operação falhou, valor inválido!")

    elif opcao == "s":
        print ("Sacar")
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Limite de saque diário excedido")
        elif excedeu_saque:
            print("Quantidade de saques diários já foi alcançada, tente novamente outro dia")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print ("Operação inválida, valor inválido!")

    elif opcao == "e":
        print ("\n==================Extrato==================")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print ("\n===========================================")

    elif opcao == "q":
        break

    else:
        print ("Opção Inválida, digite novamente a opção desejada.")
