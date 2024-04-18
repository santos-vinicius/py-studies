"""
Formatando valores com modificadores

:s - Texto (string)
:d - Inteiro (int)
:f - Float (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f_

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))

print(f'{num_1:0>10}')

nome = 'Vinicius'
sobrenome = 'Santos'
idade = '24'

nome_formatado = '{:@>50}'.format(nome)
nome_formatado2 = '{0:$^50} {1:#^50}'.format(nome, sobrenome)

print(nome_formatado)
print(nome_formatado2)

# print((50-len(nome)) / 2)

# print(f'{nome:#^50}')
