from datetime import date
nasc = int(input('Qual sua daata de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'Você tem {idade} anos')
if idade <= 9:
    print('Sua catégoria é: MIRIM')
elif idade > 9 and idade <14:
    print('Sua catégoria é: INFATIL')
elif idade > 14 and idade < 19:
    print('Sua catégoria é: JÙNIOR')
elif idade > 19 and idade < 25:
    print('Sua catégoria é: SÊNIO')
else:
    print('Sua catégoria é: MASTER')
