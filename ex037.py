numero = int(input('Digite um nùmero inteiro: '))
print('''Escolha uma das Bases para a conversão:
[1] Binario
[2]Octal
[3] Hexadecimal ''')
opicao = int(input('Sua opição: '))
if opicao == 1:
    print(f'{numero} convertido para Binario é igual a {bin(numero)[2:]} ')
elif opicao == 2:
    print(f'{numero} convertido para Octal é igual a {oct(numero)[2:]}')
elif opicao == 3:
    print(f'{numero} convertido para Hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Tente novamente!')