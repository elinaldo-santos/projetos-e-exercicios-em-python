n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2} sua media é {media}')
if media >= 5  and media < 7:
    print('Seu rendimento não foi suficiênte, você está em recuperção!')
elif media >= 7:
    print('Parabéns você foi aprovado')
elif media < 5:
    print('Infelismente você foi Reprovado!')