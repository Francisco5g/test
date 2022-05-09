from random import randint

numero_aleatorio = randint(0, 10)
 
numero_digitado = int(input('Escolha um número: '))

if numero_digitado == numero_aleatorio:
    print('Parabéns, você acertou!!')
else:
    print(f'Infelizmene você não acertou! o número era: {numero_digitado}')