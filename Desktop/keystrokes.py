from pynput.keyboard import Key, Controller


class Keystroke:
    keyboard = Controller()

    def _init_(self, keystroke):
        keyboard.press(keystroke)


key = 'a'
while key != 'b':
    if key == 'a':
        Keystroke
