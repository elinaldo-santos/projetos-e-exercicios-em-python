from datetime import date

atual = date.today().year

sexo = input('Qual é o seu sexo? [M/F] ').strip().upper()

if sexo == 'M':
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc

    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

    if idade == 18:
        print('Você tem que se alistar!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print(f'Você ainda não pode se alistar, faltam {saldo} anos.')
        print(f'Seu alistamento será em {ano}.')
    else:
        saldo = idade - 18
        ano = atual - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {ano}.')
elif sexo == 'F':
    print('Você não precisa fazer o alistamento militar.')
else:
    print('Opção inválida! Por favor, digite M para masculino ou F para feminino.')




