import win32api
import time
import win32gui
import win32con
import ctypes

#flags, hcursor, (x,y) = win32gui.GetCursorInfo()

hold = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 
                          0, 0, win32con.LR_SHARED )
hsave = ctypes.windll.user32.CopyImage(hold, win32con.IMAGE_CURSOR, 
                                       0, 0, win32con.LR_COPYFROMRESOURCE)
hnew = win32gui.LoadImage(0, 'cursor_files/mouse_up_cursor.cur', 
                             win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);
ctypes.windll.user32.SetSystemCursor(hnew, 32512)
time.sleep(15)

#restore the old cursor
ctypes.windll.user32.SetSystemCursor(hsave, 32512)