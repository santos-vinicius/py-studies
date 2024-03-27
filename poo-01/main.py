from classeAluno import Aluno

aluno1 = Aluno(nome="", matricula="", nota=float)

nome = str(input('Digite seu nome: '))
aluno1.set_nome(nome)

matricula = int(input('Digite sua matricula: '))
aluno1.set_matricula(matricula)

aluno1.media()

