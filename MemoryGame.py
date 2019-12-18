import random
import time


class MemoryGame(object):

    def __init__(self, difficulty):
        self.difficulty = difficulty


def is_list_equal(generate_list, user_list):
    try:
        status = bool(set(generate_list).intersection(user_list))
        return status
    except ValueError:
        print("ValueError: in is_list_equal")


def generate_sequence(difficulty):
    try:
        generate_list = []
        for x in range(int(difficulty)):
            generate_list.append(random.randint(1, 101))
        return generate_list
    except ValueError:
        print("ValueError: in generate_sequence")


def get_list_from_user(difficulty):
    try:
        user_list = []
        for x in range(int(difficulty)):
            user_list.append(int(input("please enter number : \n")))
        return user_list
    except ValueError:
        print("you can not insert string only integer, insert the numbers again")
        user_list.clear()
        return user_list
    except ValueError:
        print("ValueError: in get_list_from_user")


def play(difficulty):
    try:
        user_list = []
        # get sequence of numbers
        generate_list = generate_sequence(difficulty)
        # print the list for 0.7 seconds
        for y in generate_list:
            print(y, "   ", end='')
        time.sleep(1)
        print("\n" * 100)
        # os.system('ilc') need to check why it doesn't work ##########
        while len(user_list) == 0:
            user_list = get_list_from_user(difficulty)
        # compare the lists
        if is_list_equal(generate_list, user_list):
            print("Great job , you won")
            return True
        else:
            print("You lost , try again")
            return False

    except ValueError:
        print("error in play")
