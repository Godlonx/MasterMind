from pynput.keyboard import Key, Listener
from os import system, name


class Menu:

    # \033[1;<value>m Test \033[1;0m
    
    # 31 red
    # 32 green
    # 33 yellow
    # 34 blue

    def __init__(self, buttons, title = "", description = "") -> None:
        self.selection = 0
        self.buttons = buttons
        self.title = title
        self.description = description
        self.answer :str

    def on_press(self, key) -> bool:
        if key == Key.esc:
            self.selection = -1
            return False
        elif key == Key.left:
            if self.selection > 0:
                self.selection -= 1
        elif key == Key.right:
            if self.selection < len(self.buttons)-1:
                self.selection += 1
        if key == Key.enter:
            self.answer = self.buttons[self.selection]
            return False
        self.showChoices()
        

    def showChoices(self) -> None:
        # self.clear()
        printedVal = ""
        
        for index, button in enumerate(self.buttons):
            if index == self.selection:
                printedVal += f"\033[1;{31+self.selection}m" + button + "\033[1;0m"
            else:
                printedVal += button
            if index < len(self.buttons)-1:
                printedVal += " | "
        print(self.title)
        print()
        print(self.description)
        print(printedVal)
        

    def showMenu(self) -> int:
        self.showChoices()
        with Listener(on_press = self.on_press) as listener: listener.join()
        return self.selection
    
    def clear(self) -> None:
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')
