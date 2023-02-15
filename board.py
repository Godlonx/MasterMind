class gameBoard:
    def __init__(self) -> None:
        self._secretPins
        self.trials
    
    def displayGameBoard(self):
        self.diplayTrials()

    def displayTrials(self):
        for index, attempt in enumerate(self.trials):
            print(f"{index} : {attempt}")

    def displayInfo(self):
        lastTry = self.trials[len(self.trials)-1]
        # for 