users = [
  {"username": "francisco", "password": "3213"}
]

username = str(input('Nome de usuário: '))
password = str(input('Senha: '))

for user in users:
  if (user['username'] == username):
    if (user['password'] == password):
      print(f'Seja bem-vindo, {username}!')
      break

    else:
      print('Senha inválida!')

  else:
    print(f'Usuário "{username}" não encontrado!')
