nome = str(input('Qual seu nome completo: '))
print(f'O nome em maiusculo: {nome.upper()}')
print(f'O seu nome em minusculo: {nome.lower()}')
print(f'O seu tem: {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem: {nome.find(' ')}')
