V = float(input('Qual a velocidade: '))
if V > 80:
    print('Você ultrapassal a velocidade de 80KM')
    multa = (V-10)* 7
    print(f'Você deve pagar uma multa de R$:{multa:2}')
else:
    print('Boa viagem você estar na velocidade ideal.')