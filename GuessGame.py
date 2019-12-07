import random


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty


def generate_number(update_difficulty):
    try:
        return random.randint(1, int(update_difficulty))
    except:
        print("error in generate_number")


def get_guess_from_user(update_difficulty):
    guess_from_user = 0
    is_user_guessed = False
    try:
        if (int(guess_from_user) < 1) or (int(guess_from_user) > int(update_difficulty)):
            while not is_user_guessed:
                guess_from_user = int(input("please choose a number between 1 to " + str(update_difficulty) + "\n"))
                is_user_guessed = True
        return guess_from_user

    except:
        print("error in get_guess_from_user")


def compare_results(generated_number, user_guess):
    try:
        if generated_number == user_guess:
            return True  # true
        else:
            return False  # false

    except:
        print("error in  compare_results")


def play(difficulty):
    try:
        user_guess = 0
        # update the difficulty range
        update_difficulty = 2 * int(difficulty)
        # get random number
        generated_number = generate_number(update_difficulty)
        # get guess from user
        while user_guess == 0:
            user_guess = get_guess_from_user(update_difficulty)
        compared_results = compare_results(generated_number, user_guess)
        # print result
        if compared_results:
            print("Great job , you won")
        else:
            print("You lost , try again")

    except:
        print("error in play")
