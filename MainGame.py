from Live import welcome, load_game, get_chosen_game, get_game_difficulty, choose_level
import MemoryGame
import GuessGame
import CurrencyRouletteGame


class MainGame:
    welcome(name=input("Please Enter You Name:" + "\n"))

    game_number = load_game()

    difficulty = choose_level()

    if int(game_number) == 1:
        MemoryGame.play(difficulty)

    elif int(game_number) == 2:
        GuessGame.play(difficulty)

    elif int(game_number) == 3:
        CurrencyRouletteGame.play(difficulty)


#print result and add score
    if status:
        add_score(game_difficulty,user_name)
        print("Great job , you won")
    else:
        print("You lost , try again")

    p_continue = input("do you want to play again y or n ?")