import math
angulo = float(input(f'Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosceno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno de {angulo} é: {seno:.2} ')
print(f'O cosceno de {angulo} é: {cosceno:.2}')
print(f'A tangente de {angulo} é: {tangente:.2}')