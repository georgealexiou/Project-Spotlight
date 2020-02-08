import win32api
import time
import win32gui
import win32con
import ctypes

# Saving the mouse icon of value 32512, the standard arrow.
hold32512 = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 
                          0, 0, win32con.LR_SHARED )
h32512save = ctypes.windll.user32.CopyImage(hold32512, win32con.IMAGE_CURSOR, 
                                       0, 0, win32con.LR_COPYFROMRESOURCE)

# Saving the mouse icon of value 32649, the hand cursor.
hold32649 = win32gui.LoadImage(0, 32649, win32con.IMAGE_CURSOR, 
                          0, 0, win32con.LR_SHARED )
h32649save = ctypes.windll.user32.CopyImage(hold32649, win32con.IMAGE_CURSOR, 
                                       0, 0, win32con.LR_COPYFROMRESOURCE)

# Saving the mouse icon of value 32513, the I-beam.
hold32513 = win32gui.LoadImage(0, 32513, win32con.IMAGE_CURSOR, 
                          0, 0, win32con.LR_SHARED )
h32513save = ctypes.windll.user32.CopyImage(hold32513, win32con.IMAGE_CURSOR, 
                                       0, 0, win32con.LR_COPYFROMRESOURCE)

# The new mouse icon replacing the standard arrow.
h32512new = win32gui.LoadImage(0, 'cursor_files/cursor_0.cur', 
                             win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);
# The new mouse icon replacing the hand cursor.
h32649new = win32gui.LoadImage(0, 'cursor_files/cursor_1.cur', 
                             win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);
# The new mouse icon replacing the I-beam.
h32513new = win32gui.LoadImage(0, 'cursor_files/cursor_0.cur', 
                             win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);

# Updating the mouse icons.
ctypes.windll.user32.SetSystemCursor(h32512new, 32512)
ctypes.windll.user32.SetSystemCursor(h32649new, 32649)
ctypes.windll.user32.SetSystemCursor(h32513new, 32513)

time.sleep(15)

# Restore the old cursor icons.
ctypes.windll.user32.SetSystemCursor(h32512save, 32512)
ctypes.windll.user32.SetSystemCursor(h32649save, 32649)
ctypes.windll.user32.SetSystemCursor(h32513save, 32513)