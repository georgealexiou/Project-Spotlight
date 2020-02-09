from pynput.mouse import Button, Controller
import time

import win32api

import win32gui
import win32con
import ctypes

class Cursor:

    def __init__(self):

        self.controller = Controller()

        # Saving the mouse icon of value 32512, the standard arrow.
        self.hold32512 = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_SHARED )
        self.h32512save = ctypes.windll.user32.CopyImage(self.hold32512, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_COPYFROMRESOURCE)

        # Saving the mouse icon of value 32649, the hand cursor.
        self.hold32649 = win32gui.LoadImage(0, 32649, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_SHARED )
        self.h32649save = ctypes.windll.user32.CopyImage(self.hold32649, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_COPYFROMRESOURCE)

        # Saving the mouse icon of value 32513, the I-beam.
        self.hold32513 = win32gui.LoadImage(0, 32513, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_SHARED )
        self.h32513save = ctypes.windll.user32.CopyImage(self.hold32513, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_COPYFROMRESOURCE)

        # The new mouse icon replacing the standard arrow.
        self.h32512new = win32gui.LoadImage(0, 'cursor_files/cursor_0.cur', win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE)
        # The new mouse icon replacing the hand cursor.
        self.h32649new = win32gui.LoadImage(0, 'cursor_files/cursor_1.cur', win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE)
        # The new mouse icon replacing the I-beam.
        self.h32513new = win32gui.LoadImage(0, 'cursor_files/cursor_0.cur', win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE)

    # prints pointer position
    def debug(self):
        print("Mouse is at {0}".format(self.controller.position))

    # sets pointer position
    def set_position(self, x, y):
        self.controller.position = (x, y)
        print('Mouse moved to {0}'.format(self.controller.position))

    # move pointer relative to current position
    def move(self, x, y):
        self.controller.move(x, y)

    # left click the mouse
    def left_click(self):
        self.controller.click(Button.left, 1)
    
    def right_click(self):
        self.controller.click(Button.right, 1)

    # scroll mouse, ussed for changing slides
    #* dy > 0 ---> scroll down
    #* dy < 0 ---> scroll up
    #* dx = horizontal scrolling (not needed)
    def scroll(self, dx, dy):
        self.controller.scroll(dx, dy)

    # Updating the mouse icons.
    def spotlight_cursor(self):
        ctypes.windll.user32.SetSystemCursor(self.h32512new, 32512)
        ctypes.windll.user32.SetSystemCursor(self.h32649new, 32649)
        ctypes.windll.user32.SetSystemCursor(self.h32513new, 32513)

    # Restore the old cursor icons.
    def cursor_reset(self):
        ctypes.windll.user32.SetSystemCursor(self.h32512save, 32512)
        ctypes.windll.user32.SetSystemCursor(self.h32649save, 32649)
        ctypes.windll.user32.SetSystemCursor(self.h32513save, 32513)

"""
mouse = Cursor()
mouse.set_position(1000,500)
time.sleep(2)
mouse.cursor_reset()
"""
mouse = Cursor()
mouse.scroll(0,-20)