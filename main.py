from menu import Menu
from os import system, name

if __name__ == '__main__':
    testMenu = Menu(["choice 1", "choice 2", "choice 3", "choice 4"])
    testMenu.showMenu()
    if name == 'nt':
        system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')