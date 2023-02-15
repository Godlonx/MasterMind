from pynput.keyboard import Key, Listener
from os import system, name


class Menu:
    # \033[1;<value>m Test \033[1;0m
    # 30 gray
    # 31 red
    # 32 green
    # 33 yellow
    # 34 blue
    # 35 purple
    # 36 cyan
    def __init__(self, buttons, description) -> None:
        self.selection = 0
        self.buttons = buttons
        self.description = description


    def on_press(self, key):
        if key == Key.esc:
            return False
        elif key == Key.left:
            if self.selection > 0:
                self.selection -= 1
        elif key == Key.right:
            if self.selection < len(self.buttons)-1:
                self.selection += 1
        self.showChoices()
        if key == Key.enter:
            print(self.buttons[self.selection])
        

    def showChoices(self):
        self.clear()
        printedVal = ""
        for index, button in enumerate(self.buttons):
            if index == self.selection:
                printedVal += "\033[1;31m" + button + "\033[1;0m"
            else:
                printedVal += button
            if index < len(self.buttons)-1:
                printedVal += " | "
        print(printedVal)

    # Collect events until release
    def showMenu(self):
        self.showChoices()
        with Listener(on_press = self.on_press) as listener: listener.join()
    
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
