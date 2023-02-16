class Pin :
    def __init__(self, color:str, pos:int) -> None:
        self.__color:str = color
        self.__pos:int = pos

    @property
    def color(self) -> str:
        return self.__color
        
    @property
    def pos(self) -> int:
        return self.__pos