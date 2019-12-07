class Live:

    def __init__(self, difficulty):
        self.difficulty = difficulty


def welcome(name):
    print("Hello {} and welcome to the World of Games (WoG).".format(name) +
          "Here you can find many cool games to play.")
    return name


def _get_user_name():
    local_name = welcome()
    return local_name


def get_chosen_game(self):
    return self._chosen_game()


@staticmethod
def get_game_difficulty():
    return difficulty


def set_game_difficulty(self, difficulty):
    self.difficulty = difficulty


def load_game():
    min_num = 1
    max_num = 3

    try:
        print_menu()

        chosen_game = int(input("Please Enter You choice:" + "\n"))
        is_chosen_game_in_range = number_in_range(chosen_game, max_num, min_num, "chosen_game")

        if is_chosen_game_in_range:
            return chosen_game
        else:
            print("you inserted illegal value , please insert new value! " + "\n")

    except:
        print("menu except:error")


# find if the number is in the right range
def number_in_range(user_val, max_val, min_val, name):
    try:
        user_val = int(user_val)

        if int(user_val) > max_val or int(user_val) < min_val:
            print("you inserted wrong value , please insert new value! \n")
            return False
        else:
            return True
    except:
        print("you inserted illegal " + name + " value , please insert new value! \n")
        return False


def print_menu():
    print("Please choose a game to play:" + "\n" +
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back" + "\n" +
          "2. Guess Game - guess a number and see if you chose like the computer" + "\n" +
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")


def choose_level():
    min_difficulty = 1
    max_difficulty = 5
    try:
        difficulty = int(input("Please choose game difficulty from 1 to 5:" + "\n"))
        is_difficulty_in_range = number_in_range(difficulty, max_difficulty, min_difficulty, "difficulty")
        if is_difficulty_in_range:
            return difficulty
    except:
        print("problem in game_difficulty section")
    finally:
        return difficulty
