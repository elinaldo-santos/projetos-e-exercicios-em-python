nome = input('Nome do aluno: ')
nota1 = float(input('Qual é a primeira nota: '))
nota2 = float(input('Dgite a segunda nota: '))
media = nota1 + nota2 / 2
rep = media >= 6
apro = media <= 5
print(f'O aluno {nome} está com a {media}')
print(f'O aluno {nome} está reprovado ? {rep}')
print(f'O aluno está aprovado? {apro}')