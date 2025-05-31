V1 = int(input('Digite o primeiro valor: '))
V2 = int(input('Digite o segundo valor: '))
V3 = int(input('Digite o terceiro valor: '))
menor = V1
#verificando quem é menor
if V2 < V1 and V2 < V3:
    menor = V2
if V3 < V1 and V3 < V2:
    menor = V3
# verificando quem é o maior
maior = V1
if V2 > V1 and V2 > V3:
    maior = V2
if V3 > V1 and V3 > V2:
    maior = V3
print(f'O menor nùmero digitado foi {menor}')
print(f'O maior número digitado foi {maior}')