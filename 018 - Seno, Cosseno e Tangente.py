print('Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')

ângulo = float(input('ÂNGULO = '))
import math
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print(f'SENO = {seno:.2f}')
print(f'COSSENO = {cosseno:.2f}')
print(f'TANGENTE = {tangente:.2f}')