salário = int(input('Qual o salário do funcionario? R$'))
if salário <= 1.250:
    novo = salário + (salário * 15 / 100)
    print(f'O salario desse funcionario que era de {salário} agora será {novo}')
else:
    novo = salário + (salário * 10 / 100)
    print(f'Quem ganhava R${salário:2} agora reberá R${novo:2}')
