print('Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')

import math
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)
print(f'O dobro de {num} é {dobro}, o triplo é {triplo} e a raiz é {raiz}.')