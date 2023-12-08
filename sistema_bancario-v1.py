menu = """
==================================
[d] Depositar
[s] Saque
[e] Extrato
[q] Sair
=================================>
"""

saldo = 0
limite = 500
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
info_conta = []

def extrato(dados):
    i = 0
    if dados == " ":
        for elementos in info_conta:
            print(f"-{info_conta[i]}\n")
            i += 1
        print(f"Seu saldo atual é de R${saldo}.")
        
    else:
        info_conta.append(dados)

while True:
    opcao = input(menu)

    match opcao:
        case "d":
            print("Voce entrou na aba de Deposito do banco!!!\n")
            valor_depositando = int(input("Digite o valor do seu deposito: "))
            if valor_depositando > 0:
                print(f"Seu deposito de R${valor_depositando} foi realizado com sucesso")
                saldo += valor_depositando
                send_extrato = f"Foi depositado R${valor_depositando}."
                extrato(send_extrato)
            else:
                print("ERROR -Informe um valor maior de 0-")
        case "s":
            print("Voce entrou na aba de Saque do banco!!!\n")
            valor_do_saque = int(input("Digite o valor desejado para o saque: "))
            if (valor_do_saque < saldo) and (numero_de_saques < LIMITE_DE_SAQUES) and (valor_do_saque <= limite):
                saldo -= valor_do_saque
                numero_de_saques += 1
                limite -= valor_do_saque
                send_extrato = f"Saque de R${valor_do_saque} realizado. Seu saldo é de R${saldo}"
                extrato(send_extrato)
                print(f"O seu saque de R${valor_do_saque} foi realizado com sucesso")
            elif valor_do_saque > saldo:
                print("ERROR!! -Saldo insuficente-")
            elif valor_do_saque > limite:
                print("ERROR -Seu limite de saques em dinhero foi atinjido-")
            else:
                print("ERROR -Voce ultrapassou o seus limites de saque dirarios-")
        case "e":
            send_extrato = " "
            extrato(send_extrato)
        case "q":
            print("Muito obrigado por usar nosso sistema de bancos SISCRED")
            break
        case _:
            print("invalido. Inssira uma opção correta")