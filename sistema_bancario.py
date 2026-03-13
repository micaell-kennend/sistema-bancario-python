print('Olá, Iremos criar sua conta bancária!')
nome = input('Me fale o nome que você prefere ser chamado!')
print(f' A partir de agora {nome}, você terá que depositar um valor para ativação da sua conta!')
saldo = float(input('Digite o Valor!'))
print(f'Deposito de R$ {saldo}, realizado com sucesso' )

def ver_saldo(saldo):
      print(f'Seu saldo é de R${saldo}')

def depositar(saldo):
     valor = float(input('Digite um valor que deseja depositar:'))
     saldo = saldo + valor
     print(f'Depósito de R${valor} realizado com sucesso!')
     print(f'Seu saldo atual é R${saldo}')
     return saldo

def sacar(saldo):
    valor = float(input('Qual valor deseja sacar? '))

    if valor > saldo:
      print("Saldo insuficiente")
    else:
        saldo = saldo - valor
        print(f'Saque de R${valor} realizado com sucesso!')
        print(f'Seu saldo atual é R${saldo}')

    return saldo

while True:

    print('\n--- MENU ---')
    print('saldo')
    print('deposito')
    print('sacar')
    print('sair')

    opcao = input('Escolha uma opção: ')

    if opcao == "saldo":
        ver_saldo(saldo)

    elif opcao == "deposito":
        saldo = depositar(saldo)

    elif opcao == "sacar":
        saldo = sacar(saldo)

    elif opcao == "sair":
        print('Sistema encerrado.')
        break