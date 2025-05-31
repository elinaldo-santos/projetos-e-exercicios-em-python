print('=' * 20)
print('   LOJA E.SANTOS   ')
print('=' * 20)
preco = float(input('Preço das compras R$: '))
print('''FORMAS DE PAGAMENTO
[1] á vista, dinheiro ou check.
[2] á vista no cartão
[3] 2 x no cartão
[4] 3x ou mais no cartão''')
opicao = int(input('Qual a opição? '))
if opicao == 1:
    total = preco - (preco * 10 / 100)
elif opicao == 2:
    total = preco - (preco * 5 / 100)
elif opicao == 3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada de 2x de {parcela} no cartão de credito sem juros.')
elif opicao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua parcela será parcelada em {totparc}x de  R${parcela} com juros.')
print(f'Sua compra de R${preco} vai custar R${total} no final.')
