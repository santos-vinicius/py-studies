class Aluno:
  
  def __init__(self, nome, matricula, nota) -> None:
    pass
    self.nome = nome 
    self.matricula = matricula
    self.nota = nota
    
  def get_nome(self):
    return self.nome
  
  def set_nome(self, nome):
    self.nome = nome 
    
  def get_matricula(self):
    return self.matricula
  
  def set_matricula(self, matricula):
    self.matricula = matricula
  
  def get_nota(self):
    return self.nota

  def set_nota(self, nota):
    self.nota = nota
    
  def media(self):
    media = 0
     
    contador = int(input('Digite a quantidade de notas que deseja saber a média: '))
    for x in range(0, contador, +1): 
      self.get_nota = float(input('Digite a nota: '))
      media = media + self.get_nota / contador
    print(f'Sua média é {media}')
    
    if(media < 6):
        print(f"REPROVADO")
    else:
      print("APROVADO")