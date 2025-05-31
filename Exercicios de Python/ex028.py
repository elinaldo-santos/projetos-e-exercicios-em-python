from random import randint # faz com que o computador sortei um numero aleatorio.
from time import sleep  # faz com que o computador tipo dormice por alguns segundos.
computador = randint(0,5)# faz o computador "PENSAR"
print('-=-'* 18)
print('Vou pemsar em um numéro de 0 a 5, tente adivinhar...')
print('-=-'* 18)
jogador = int(input('Em que numéro eu pensei? ')) #faz o jogador advinhar
print('PROCESSANDO....')
sleep(3)
if jogador == computador:
    print('Você Ganhou!')
else:
    print(f'Ganhei!Eu pensei no numero {computador} e não no numero {jogador}')