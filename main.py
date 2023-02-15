from random import randint
from pynput.keyboard import Key, Listener


class Menu:
    def __init__(self) -> None:
        self.selection = 0


    def on_press(self, key):
        print('{0} pressed'.format(
            key))
        
        if key == Key.esc:
            # Stop listener
            return False
        elif key == Key.left:
            if self.selection > 0:
                self.selection -= 1
        elif key == Key.right:
            if self.selection < 10:
                self.selection += 1
        elif key == Key.enter:
            print(self.selection, " select")
        print(self.selection)

    def on_release(self, key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False 

    # Collect events until released
    def startMenu(self):
        with Listener(
                on_press = self.on_press
                ) as listener:
            listener.join()


if __name__ == '__main__':
    menuTest = Menu()
    menuTest.startMenu()