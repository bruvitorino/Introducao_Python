print('Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.')

numero = int(input('Digite um número: '))
print(f'TABUADA DO {numero}')
print('=' * 15)
for c in range(1,11):
    print(f'{numero:2} * {c:2} = {numero * c:2}')
print('=' * 15)