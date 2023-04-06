print('Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

primeiro = str(input('Digite o nome do primeiro aluno(a): '))
segundo = str(input('Digite o nome do segundo aluno(a): '))
terceiro = str(input('Digite o nome do terceiro aluno(a): '))
quarto = str(input('Digite o nome do quarto aluno(a): '))
from random import shuffle
lista = [primeiro, segundo, terceiro, quarto]
sorteado = shuffle(lista)
print('A ordem de apresentação será:')
print(lista)