class pins :
    def __init__(self) -> None:
        self._color
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        possiblesColors = ["Blue", "Green", "Red", "Yellow", "Orange", "Purple"]

        if color in possiblesColors:
            self._color = color
        else:
            return "Not a valid color"
    
    def get_pos(self):
        return self._pos