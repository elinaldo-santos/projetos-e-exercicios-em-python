from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analisar o ano atual: 0 '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bixesto')
else:
    print(f'O ano {ano} não é bixesto ')