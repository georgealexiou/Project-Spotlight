from pynput.mouse import Button, Controller
import time

import win32api
import time
import win32gui
import win32con
import ctypes

class Mouse:

    def _init_():
        self.controller = Controller()
        win_cursor_red()

    # prints pointer position
    def debug(self):
        print("Mouse is at {0}".format(mouse.position))

    # sets pointer position
    def set_position(self, x, y):
        mouse.position = (x, y)
        print('Mouse moved to {0}'.format(mouse.position))

    # move pointer relative to current position
    def move(self, x, y):
        mouse.move(x, y)

    # left click the mouse
    def left_click(self):
        mouse.click(Button.left, 1)
        win_cursor_blue()
    
    def right_click(self):
        mouse.click(Button.right, 1)
        win_cursor_blue()

    # press mouse for x amount of seconds
    def press(self, seconds):
        mouse.press(Button.left)
        win_cursor_blue()
        time.sleep(seconds)
        mouse.release(Button.left)

    # scroll mouse, ussed for changing slides
    #* dy > 0 ---> scroll down
    #* dy < 0 ---> scroll up
    #* dx = horizontal scrolling (not needed)
    def scroll(self, dx, dy):
        mouse.scroll(dx, dy)


    #! idk if this works we need to test it
    #change to red
    def win_cursor_red():
        hold = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_SHARED )
        hsave = ctypes.windll.user32.CopyImage(hold, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_COPYFROMRESOURCE)
        hnew = win32gui.LoadImage(0, 'cursor_files/mouse_up_cursor.cur', win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);
        ctypes.windll.user32.SetSystemCursor(hnew, 32512)
    
    #change to blue
    def win_cursor_blue():
        hold = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_SHARED )
        hsave = ctypes.windll.user32.CopyImage(hold, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_COPYFROMRESOURCE)
        hnew = win32gui.LoadImage(0, 'cursor_files/mouse_down_cursor.cur', win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);
        ctypes.windll.user32.SetSystemCursor(hnew, 32512)

    # change to up arrow
    def win_cursor_scroll_up():
        pass

    # change to down arrow
    def win_cursor_scroll_down():
        pass

    #reset to normal
    def win_cursor_reset():
        ctypes.windll.user32.SetSystemCursor(hsave, 32512)


mouse = Mouse()
set_position(100,100)
win_cursor_blue()
time.sleep(2)
win_cursor_reset()