aluno = input('Nome do aluno:')
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota:'))
media = (n1 + n2 + n3) / 3
print(f'Olá seu {aluno} sua media é: {media:2}')
if media >= 6:
    print('Parabéns você foi aprovado!')
elif media <= 5 and media >= 4:
    print('Infelismente você estar em RECUPERAÇÃO')
else:
    print('REPROVADO')

