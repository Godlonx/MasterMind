class Trial:
    def __init__(self) -> None:
        self.__pins = []
        self.indications = {"goodPos":0, "goodColor":0}

    @property
    def pins(self):
        return self.__pins
      
    def add_pins(self, pin):
        self.__pins.append(pin)