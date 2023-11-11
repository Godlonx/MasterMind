from trial import Trial
from pin import Pin
from menu import Menu
from random import randint
from os import system, name


class GameBoard:
    def __init__(self) -> None:
        self.trials :list = []
        self.possibleColors = ["Red", "Green", "Yellow", "Blue"]
        self.attempts = 12
        self.__secretPins :list[Pin] = []
            
    def newTry(self):
        newTry = Trial()
        for pos in range(5):
            description = self.displayTrials()
            description += "\n"
            if len(newTry.pins)> 0:
                for pin in newTry.pins:
                    description += pin.color + " "
            colorSelectMenu = Menu(self.possibleColors, f"Select a color for the hole {pos}", description)
            choosedColor = colorSelectMenu.showMenu()
            if choosedColor >= 0:
                newPin = Pin(f"\033[1;{31+choosedColor}m⬤\033[1;0m ", pos)
                newTry.add_pins(newPin)
            else:
                self.Stop()
        self.checkCombination(newTry)
        self.trials.append(newTry)
    
    def checkCombination(self, trial:Trial) -> None:
        pins = trial.pins.copy()
        for secretPin in self.__secretPins:
            if secretPin.color == trial.pins[secretPin.pos].color:
                trial.indications["goodPos"] += 1
            else :
                pins2 = pins.copy()
                do = True
                for index, pin in enumerate(pins2):
                    if do:
                        if pin.color == secretPin.color and pin.pos != secretPin.pos:
                            trial.indications["goodColor"] += 1
                            del pins[index]
                            do = False
                print(pins)
        if trial.indications["goodPos"] == 5:
            self.Win()
        else:
            self.attempts -= 1

    def displayTrials(self) -> str:
        attempt:Trial
        displayTable = [[" "*28, "TRIALS", " "*28, "Secret Code"],["╒════", "╤════"*11,"╕"]]
        line = ""
        for i in range(5):
            line = "│"
            for attempt in self.trials:
                line += " " + attempt.pins[i].color + " │"
            for _ in range(12-len(self.trials)):
                line += "    │"
            displayTable.append([line])
        displayTable.append(["╞════", "╪════"*11,"╡"])
        for j in range(5):
            line = "│"
            for i in range(len(self.trials)):
                goodPos = self.trials[i].indications["goodPos"]
                goodColor = self.trials[i].indications["goodColor"]
                if goodPos >= j:
                    line += " \033[1;35m⬤\x1b[1;0m  │"
                elif goodColor > j-goodPos:
                    line += " \033[1;37m⬤\x1b[1;0m  │"
                else:
                    line += "    │"
            for _ in range(12-len(self.trials)):
                line += "    │"
            displayTable.append([line])
        displayTable.append(["╘════", "╧════"*11,"╛"])
        text = ""
        for i in displayTable:
            line = ""
            for j in i:
                line += j
            text += line + "\n"
        return text
            
    def selectSecretComb(self):
        for pos in range(5):
            selectedColor = randint(0, 3)
            self.__secretPins.append(Pin(f"\033[1;{31+selectedColor}m⬤\033[1;0m ", pos))
        
    def game(self):
        self.selectSecretComb()
        while self.attempts > 0:
            self.newTry()
            
    def Win(self):
        colors = ""
        for pin in self.__secretPins:
            colors += pin.color + " "
        print(f"Good job you find the right combination : {colors}")
        self.Stop()
        
    def Lose(self):
        colors = ""
        for pin in self.__secretPins:
            colors += pin.color + " "
        print(f"Nice try but the right combination was {colors}")
        self.Stop()
    
    def Stop(self):
        self.displayTrials()
        val = input("")
        raise SystemExit
    
    def clear(self) -> None:
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')
