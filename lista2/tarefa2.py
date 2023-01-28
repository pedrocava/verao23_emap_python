import random

def jogadaNivelFacil() -> str:

    return random.choice(['pedra', 'papel', 'tesoura'])

def jogadaNivelMedio(p_pedra: float, p_tesoura: float, p_papel: float) -> str:

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

    print("Você escolhei o nível {}".format(difficulty_level))

    n_rounds = 0
    player_won = 0
    computer_won = 0
    draws = 0

    played_pedras = 0
    played_papel = 0
    played_tesoura = 0

    if difficulty_level == "1":

        move = input("Digite pedra, tesoura ou papel para fazer sua jogada. Digite ‘sair’ para terminar o jogo.")

        if move == "pedras":

            played_pedras == played_pedras + 1

        elif move == "papel":

            played_papel = played_papel + 1

        elif move == "tesoura":

            played_tesoura = played_tesoura + 1

        while move != "sair":

            computer_move = jogadaNivelFacil()

            print("Minha jogada foi {}".format(computer_move))

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







        





