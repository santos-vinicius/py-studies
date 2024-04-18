"""
While em Python - Aula 07 
Utilizando para realizar ações enquanto uma condição for verdadeira.

Requisitos: Entender condições e operadores.
"""
# While =>  Enquanto 

# while True:  # loop infinito
#   nome = input("Qual o seu nome?")
#   print(f'Olá {nome}!')

# print("Não será executada!")

"""
continue: pula para o próximo laço de repetição, cuidado para não criar
laços infinitos

break:  interrompe a execução do laço de repetição
"""

num = 0 #Loop normal
while num <= 10: 
  if num == 3:
    num = num + 1 
    # break
    continue 
  
  print(num)
  num = num + 1   

print("Acabou!")

print('----------------------------------')

x = 0 # coluna
while x < 10:
  y = 0 # linha
  while y < 5: 
    print(f'X vale {x} e Y vale {y}')
    y += 1 
  x += 1 # x = x + 1  

print('Acabou!')  

