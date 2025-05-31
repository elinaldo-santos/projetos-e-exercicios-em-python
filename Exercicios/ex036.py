casa = float(input('Qual o valor da casa R$:'))
salario = float(input('Qual seu salario R$:'))
anos = int(input('Uqantos anos de finaciamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa} em {anos} anos')
print(f'A prestação será de R${prestacao}')
if salario <= minimo:
    print('O seu emprestimo foi aprovado!')
else:
    print('O seu salario não foi aprovado!')