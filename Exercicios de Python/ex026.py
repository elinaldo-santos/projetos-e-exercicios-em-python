frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A primeira letra A pareceu na posição {frase.find('A') + 1}')
print(f'A ultima letra A apareceu na {frase.rfind('A') + 1} posição')