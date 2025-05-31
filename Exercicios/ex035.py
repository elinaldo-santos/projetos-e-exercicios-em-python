r1 = float(input('Qual o primeiro seguimento: '))
r2 = float(input('Qual o segundo seguimento: '))
r3 =float(input('Qual o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triângulo!')
else:
    print('Os triâgulos acima não formam triângulo!')
