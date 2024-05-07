"""
Luiz Otávio Miranda - EXERCICIO - Tamanho do Nome 

Faça um código que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 letras escreva "Seu nome é grande
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
  if tamanho_nome <= 4:
    print('Seu nome é curto!')
  elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu npme é normal')
  else:
    print('Seu nome é grande')
else:
  print('Por favor, digite pelo mais de uma letra.')