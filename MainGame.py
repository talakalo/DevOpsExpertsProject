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
