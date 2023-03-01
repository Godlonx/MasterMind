from menu import Menu
from os import system, name
from pin import Pin
from board import GameBoard
if __name__ == '__main__':
    newBoard = GameBoard()
    newBoard.game()
    # displayTable = [[" "*28, "TRIALS", " "*28, "Secret Code"],["╒════", "╤════"*11,"╕"]]
    # for _ in range(6):
    #     displayTable.append(["│ \033[1;37m⬤\x1b[1;0m  "*12, "│"])
    # displayTable.append(["╘════", "╧════"*11,"╛"])
    # # print(displayTable)
    # for i in displayTable:
    #     text = ""
    #     for j in i:
    #         text += j
    #     print(text)