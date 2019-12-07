import random
import Live
import time


class MemoryGame(object):

    def __init__(self, difficulty):
        self.difficulty = difficulty


def is_list_equal(generate_list, user_list):
    try:
        status = bool(set(generate_list).intersection(user_list))
        return status
    except:
        print("error in is_list_equal")


def generate_sequence(difficulty):
    try:
        generate_list = []
        for x in range(int(difficulty)):
            generate_list.append(random.randint(1, 101))
        return generate_list
    except:
        print("error in generate_sequence")


def get_list_from_user(difficulty):
    try:
        user_list = []
        for x in range(int(difficulty)):
            user_list.append(int(input("please enter number : \n")))
        #        user_list = input("please enter the number split by ,")
        return user_list
    except ValueError:
        print("you can not insert string only integer, insert the numbers again")
        user_list.clear()
        return (user_list)
    except:
        print("error in MG get_list_from_user")


def play(difficulty):
    try:
        user_list = []
        # get sequance of numbers
        generate_list = generate_sequence(difficulty)
        # print the list for 0.7 seconds
        for y in generate_list:
            print(y, "   ", end='')
        time.sleep(1)
        print("\n" * 100)
        # os.system('ilc') need to check why it doesn't work ##########
        while len(user_list) == 0:
            user_list = get_list_from_user(difficulty)
        # compre the lists
        status = is_list_equal(generate_list, user_list)
        if status:
            print("Great job , you won")

        else:
            print("You lost , try again")

    except:
        print("error in play")
    # def is_list_equal(self):
    #     list_from_user = self.get_list_from_user()
    #     generated_list = self.generate_sequence()
    #     return list_from_user.__eq__(generated_list)
# def get_list_from_user():
#     return list_from_user

# def get_list_from_user(self):
#     # self.difficulty = len(generate_sequence())
#     list_from_user = self.difficulty
#     try:
#
#         while len(list_from_user) != self.difficulty:
#             list_from_user.append(
#                 int(input("Please Insert Your List Of Numbers Between 1 To {}".format(self.difficulty * 2) + "\n")))
#     except:
#         print('except: ' + list_from_user + 'self.difficulty +2: ' + self.difficulty * 2)
#     finally:
#         return list_from_user
# def play(self):
#     if self.is_list_equal():
#         print("You Win")
#     else:
#         print("You Lose Try Again")
