print('Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.')

primeiro = str(input('Digite o nome do primeiro aluno(a): '))
segundo = str(input('Digite o nome do segundo aluno(a): '))
terceiro = str(input('Digite o nome do terceiro aluno(a): '))
quarto = str(input('Digite o nome do quarto aluno(a): '))
from random import choice
lista = [primeiro, segundo, terceiro, quarto]
sorteado = choice(lista)
print(f'O aluno(a) sortedo foi {sorteado}.')