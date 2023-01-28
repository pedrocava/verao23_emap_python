import random

def jogadaNivelFacil() -> str:

    return random.choice(['pedra', 'papel', 'tesoura'])

def jogadaNivelMedio(p_pedra: float, p_papel: float, p_tesoura: float) -> str:


    print(f"""Debug! Os pesos passados para jogadaNivelMedio são:
      {p_pedra} para pedra, {p_papel} para papel e {p_tesoura} para tesoura""")

    draw = random.choices(
      ['pedra', 'papel', 'tesoura'],
      [p_pedra, p_papel, p_tesoura])

    return draw[0] # random.choices returns a a list with a single element

def who_won(user, computer):

    if user == computer:

        return "draw"

    elif user == "pedra":

        if computer == "papel":

            return "computer"
        
        elif computer == "tesoura":

            return "user"

    elif user == "papel":

        if computer == "pedra":

            return "user"
        
        elif computer == "tesoura":

            return "computer"

    elif user == "tesoura":

        if computer == "papel":

            return "user"

        elif computer == "pedra":

            return "computer"

def main():

    player_name = input(
      "Olá! Bem-vindo(a) ao jogo Pedra, Tesoura e Papel. Por favor, digite o seu nome: ")

    difficulty_prompt = """{}, por favor, informe qual nível de jogo você gostaria de jogar.
        Digite 1 para fácil ou 2 para médio:""".format(player_name)

    difficulty_level = input(difficulty_prompt)

    print("Você escolheu o nível {}".format(difficulty_level))

    n_rounds = 0
    player_won = 0
    computer_won = 0
    draws = 0

    played_pedra = 0
    played_papel = 0
    played_tesoura = 0

    computer_played_pedra = 0
    computer_played_papel = 0
    computer_played_tesoura = 0

    move = input("Digite pedra, tesoura ou papel para fazer sua jogada. Digite ‘sair’ para terminar o jogo.")

    while move != "sair":

        # Counting player moves

        if move == "pedra":

            played_pedra = played_pedra + 1

        elif move == "papel":

            played_papel = played_papel + 1

        elif move == "tesoura":

            played_tesoura = played_tesoura + 1

        # Chosing computer move

        if difficulty_level == "1":

            computer_move = jogadaNivelFacil()

        elif difficulty_level == "2":

            if n_rounds == 0:

              w_pedra = 1
              w_papel = 1
              w_tesoura = 1

            else:

              w_pedra = played_pedra / n_rounds
              w_papel = played_papel / n_rounds
              w_tesoura = played_tesoura / n_rounds

            computer_move = jogadaNivelMedio(w_pedra, w_papel, w_tesoura)

        print("Minha jogada foi {}".format(computer_move))

        # Counting computer moves

        if computer_move == "pedra":

            computer_played_pedra == computer_played_pedra + 1

        elif computer_move == "papel":

            computer_played_papel = computer_played_papel + 1

        elif computer_move == "tesoura":

            computer_played_tesoura = computer_played_tesoura + 1

        result = who_won(move, computer_move)

        if result == "computer":

            print("Ops! Eu ganhei desta vez!")

            computer_won = computer_won + 1
            
        elif result == "draw":

            print("Ufa! Foi empate!")

            draws = draws + 1

        elif result == "user":

            print("Parabéns, {}, você ganhou esta rodada!".format(player_name))

            player_won = player_won + 1

        n_rounds = n_rounds + 1

        move = input("Digite pedra, tesoura ou papel para fazer sua jogada. Digite ‘sair’ para terminar o jogo.")

    if player_won > computer_won:

        winner = player_name

    elif computer_won > player_won:

        winner = "Computador"

    elif computer_won == player_won:

        winner = "Empatado"

    endgame_message = f"""
    *** Fim do Jogo ***

    Vencedor: {winner}
    Número de rodadas: {n_rounds}
    Número de rodadas que você venceu: {player_won}
    Número de empates: {draws}
    Suas jogadas: 
    Minhas Jogadas:
    """

    print(endgame_message)
        






        





