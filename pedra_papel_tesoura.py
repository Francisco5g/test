import random

game_name = ['pedra', 'papel', 'tesoura']

while True:
    player1 = str(input('Pedra, Papel ou Tesoura?: ')).lower()
    player2 = game_name[random.randint(0, len(game_name) - 1)]

    if player1 == '': 
        continue

    if player1 == player2:
        print('Empate!!')


    # 1 -> win; -1 -> lose
    choose = {
        "pedra": {
            "papel": -1,
            "tesoura": 1
        },
        "papel": {
            "pedra": 1,
            "tesoura": -1
        },
        "tesoura": {
            "papel": 1,
            "pedra": -1
        }
    }

    if choose[player1][player2] < 0:
        print(f"Você perdeu! (Você: {player1}; Adversário: {player2})")

    else:
        print(f"Você ganhou! (Você: {player1}; Adversário: {player2})")
