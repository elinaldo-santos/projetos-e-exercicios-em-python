from random import randint
from time import sleep
itens = ('Pedra','Papel','tesoura')
computador  = randint(0,2)
print('''Suas Opções:
[1]Pedra
[2]Papel
[3]Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep (1)
print('KEM')
sleep(1)
print('PO')
print('-=' * 12)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 12)
if computador == 0: #computador jogou pedra
   if jogador == 0:
       print('EMPATE')
   elif jogador == 1:
       print('JOGADOR VENCE')
   elif jogador == 2:
       print('COMPUTADOR VENCER')
   else:
       print('Jogada invalida')
elif computador ==1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')
else:
  print('JOGADA INVALIDA')