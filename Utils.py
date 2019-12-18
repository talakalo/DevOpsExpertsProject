from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Utils:

    @staticmethod
    def screen_cleaner():
        try:
            if name == 'nt':
                _ = system('cls')

                # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')
        except IOError:
            print("Failed to Clean The  Screen Please Check")
