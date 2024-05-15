"""
Iterando strings com while
"""

nome = 'Vinicius Santos' #Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
  letra = nome[indice]
  novo_nome += f'*{letra}' # *V*i*n*i*c*i*u*s* *S*a*n*t*o*s
  indice += 1 

print(novo_nome)