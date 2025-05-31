Nome = str(input('Seu nome é: '))
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual é a altura: '))
imc = peso/ (altura ** 2)
print(input(f'Olá seu {Nome}, Obrigado pela confiança do nosso sistema'))
if imc <= 18.5:
    print('Abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('SobrePeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mornia')