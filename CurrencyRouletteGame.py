from random import randint
from forex_python.converter import CurrencyRates


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty


def get_guess_from_user(self, amount_in_usd):
    user_guess = int(input(f'How much do you think {amount_in_usd}$ is in ILS?').format(amount_in_usd))
    while 0 > user_guess > self.MAX_AMOUNT:
        user_guess = int(input(f'Please only enter an amount between 0 and {self.MAX_AMOUNT}'))
    return user_guess


def get_money_interval(difficult):
    try:
        # getCurrency Rate
        c = CurrencyRates()
        currency_rate = c.get_rate('USD', 'ILS')
        # get random number between 1-100
        random_number = randint(1, 100)
        total_amount = random_number * currency_rate
        interval = 5 - int(difficult)

        dict_currency = {
            "currency_rate": currency_rate,
            "random_number": random_number,
            "total_amount": total_amount,
            "interval": interval
        }
        return dict_currency
    except ValueError:
        print("ValueError: in get_money_interval")


def get_guess_from_user(random_number):
    try:
        user_guess = -1
        while user_guess < 1:
            user_guess = int(input("How Many NIS Is " + str(random_number) + " $: \n"))
            if user_guess < 1:
                print("number must be positive")
        return user_guess
    except ValueError:
        print(" you must insert number")
        return 0
    except ValueError:
        print("ValueError: in get_guess_from_user")


def play(difficult):
    try:
        user_guess = 0
        dict_currency = get_money_interval(difficult)
        # for x in dict.values():
        #   print(x)
        while user_guess == 0:
            user_guess = get_guess_from_user(dict_currency.get("random_number"))
            # check user guess
            exchanged_total_amount = int(dict_currency.get("total_amount"))
        interval = int(dict_currency.get("interval"))
        if int(exchanged_total_amount) - int(interval) <= int(user_guess) <= int(exchanged_total_amount) + \
                int(interval):
            print("Great job , you won")
            return True
        else:
            print("You lost , try again")
            return False

    except ValueError:
        print("ValueError: in Play")
