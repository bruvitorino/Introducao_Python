print('Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')

km = float(input('Qual a quilometragem percorrida? '))
dias = int(input('Quantos dias pretende ficar com o carro? '))
variavel_01 = dias * 60
variavel_02 = km * 0.15
custo_total = variavel_01 + variavel_02
print(f'O aluguel custa R$ {custo_total}')