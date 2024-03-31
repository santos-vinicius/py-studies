"""
Operadores relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente de
"""

# Exercício emprestimo

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

idade = int(idade)
# Limite para pegar emprestimo
idade_menor = 18  # jovem demais
idade_maior = 40  # passou a idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo!')
else:
    print(f'{nome} não pode pegar o empréstimo!')
