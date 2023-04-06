print('Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

preço = float(input('Digite o valor do produto: R$ '))
preço_com_desconto = preço * 0.95
print(f'O valor com desconto é R$ {preço_com_desconto}.')