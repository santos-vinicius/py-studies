frase = 'Vinicius Santos'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
  letra_atual = frase[1] 
  
  if letra_atual == ' ':
    i += 1
    continue 
  
  qtd_vezes_apareceu = frase.count(letra_atual)

  if apareceu_mais_vezes < qtd_vezes_apareceu:
    apareceu_mais_vezes = qtd_vezes_apareceu
    letra_apareceu_mais_vezes = letra_atual
  
  i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" que apareceu {apareceu_mais_vezes}x.')
