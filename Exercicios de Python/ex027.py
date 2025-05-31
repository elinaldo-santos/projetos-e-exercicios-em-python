n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(F'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')