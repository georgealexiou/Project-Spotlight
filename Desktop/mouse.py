from pynput.mouse import Button, Controller
import time

class Mouse:

    def _init_():
        self.controller = Controller()

    # prints pointer position
    def debug(self):
        print("Mouse is at {0}".format(mouse.position))

    # sets pointer position
    def set_position(self, x, y):
        mouse.position = (x, y)
        print('Mouse moved to {0}'.format(mouse.position))

    # move pointer relative to current position
    def move(self):
        mouse.move(5, -5)

    # left click the mouse
    def left_click(self):
        mouse.click(Button.left, 1)
    
    def right_click(self):
        mouse.click(Button.right, 1)

    # press mouse for x amount of seconds
    def press(self, seconds):
        mouse.press(Button.left)
        time.sleep(seconds)
        mouse.release(Button.left)

    # scroll mouse, ussed for changing slides
    # * dy > 0 ---> scroll down
    # * dy < 0 ---> scroll up
    # * dx = horizontal scrolling (not needed)
    def scroll(self, dx, dy):
        mouse.scroll(dx, dy)