from pynput.mouse import Button, Controller
#import pyautogui
import time

mouse = Controller()

# screen resolution
#width, height = pyautogui.size()

# prints pointer position
def debug():
    print("Mouse is at {0}".format(mouse.position))

# sets pointer position
def set_position(x, y):
    mouse.position = (x, y)
    print('Mouse moved to {0}'.format(mouse.position))

# move pointer relative to current position
def move():
    mouse.move(5, -5)

# click the mouse
def click():
    mouse.click(Button.left, 1)

# press mouse for x amount of seconds
def press(seconds):
    mouse.press(Button.left)
    time.sleep(seconds)
    mouse.release(Button.left)

# scroll mouse, ussed for changing slides
# * dy > 0 ---> scroll down
# * dy < 0 ---> scroll up
# * dx = horizontal scrolling (not needed)
def scroll(dx, dy):
    mouse.scroll(dx, dy)

time.sleep(3)
scroll(0,1)