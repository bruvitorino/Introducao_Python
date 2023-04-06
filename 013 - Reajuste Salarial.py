print('\033[7;30mFaça um algaritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.\033[m')

salario = float(input('\nDigite o salário R$ '))

aumento = 1.15 * salario

print(f'Salário com reajuste é de R$ {aumento:.2f} ')