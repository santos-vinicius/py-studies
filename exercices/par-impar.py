"""
LOM - EXERCICIO - PAR OU IMPAR 

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro. 
"""

entrada = input('Digite um numero: ')

if entrada.isdigit():
  entrada_int = int(entrada)
  par_impar = entrada_int % 2 == 0
  par_impar_texto = 'impar'
  
  if par_impar: 
    par_impar_texto = 'par'
  
  print(f'O número {entrada_int} é {par_impar_texto}')
  ...
else:
  print('Voce não digitou um numero inteiro')