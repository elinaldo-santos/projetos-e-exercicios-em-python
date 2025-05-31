distancia = float(input('Qual a istância da viagem? '))
print(f'Você estar prestes a começar uma viagem de {distancia}KM')
if distancia <= 200:
    preco = distancia*0.50
    print(f'Sua viagem custará R$:{preco:2}')

else:
    preco = distancia*0.45
    print(f'Sua viagem custará R$:{preco:2}')