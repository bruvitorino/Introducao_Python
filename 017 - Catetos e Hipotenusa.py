print('Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.')

cateto_adjacente = int(input('Digite o valor do CATETO ADJACENTE: '))
cateto_oposto = int(input('Digite o valor do CATETO OPOSTO:'))
import math
calculo = (cateto_adjacente**2) + (cateto_oposto**2)
hipotenusa = math.sqrt(calculo)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')