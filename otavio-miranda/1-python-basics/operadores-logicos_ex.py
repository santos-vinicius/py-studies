# Exemplo de operador lógico

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'vinicius'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Acesso Permitido')
else:
    print('Acesso Negado')