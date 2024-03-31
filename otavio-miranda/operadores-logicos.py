"""
Operadores Lógicos
and, or, not
in e not in
"""

A = 2
B = 2
C = 3

compara = A == B and B < C
print(compara)

compara2 = A == B or B < C
print(compara2)

compara3 = not A == B and not B < C
print(compara3)

# (Verdadeiro e Falso)
comparacao1 and comparacao2

# Verdadeiro ou Verdadeiro
comparacao1 or comparacao2

a = 2
b = 3

if b > a:
    print('B é maior que A')
else:
    print('A é maior que B')

nome = 'Vinicius'

if 'u' in nome:
    print('Existe a letra U no seu nome.')
else:
    print('Não existe.')