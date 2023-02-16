from trial import Trial
from pin import Pin
from menu import Menu
from random import randint
from os import system, name


class GameBoard:
    def __init__(self) -> None:
        self.__secretPins :list = []
        self.trials :list = []
        self.possibleColors = ["Blue", "Green", "Red", "Yellow"]
        self.attempts = 12
            
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
            if choosedColor != "Exit":
                newPin = Pin(choosedColor, pos)
                newTry.add_pins(newPin)
            else:
                self.Stop()
        self.checkCombination(newTry)
        self.trials.append(newTry)
    
    def checkCombination(self, trial:Trial) -> None:
        pins = self.__secretPins.copy()
        for pin in trial.pins:
            tmpPins = pins.copy()
            for index, secretPin in enumerate(tmpPins):
                if pin.color == secretPin.color:
                    if pin.pos == secretPin.pos:
                        trial.indications["goodPos"] += 1
                    elif pin.color == secretPin.color:
                        trial.indications["goodColor"] += 1
                    del pins[index]
                    break
                        
        if trial.indications["goodPos"] == 5:
            self.Win()
        else:
            self.attempts -= 1

    def displayTrials(self) -> str:
        attempt:Trial
        text:str = ""
        for index, attempt in enumerate(self.trials):
            info = ""
            for pin in attempt.pins:
                info += pin.color + " "
            info += "| "
            goodPos = attempt.indications["goodPos"]
            goodColor = attempt.indications["goodColor"]
            info += " good Pos : " + str(goodPos) + ", goodColor : " + str(goodColor)
            text += f"{index} : {info}\n"
        return text
            
    def selectSecretComb(self):
        for pos in range(5):
            selectedColor = self.possibleColors[randint(0, 3)]
            self.__secretPins.append(Pin(selectedColor, pos))
        
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
        raise SystemExit
    
    def clear(self) -> None:
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')
