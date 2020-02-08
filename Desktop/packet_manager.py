import mouse.py as Mouse
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

mouse = Mouse.Mouse()

def _init_(message):
try
    # clicks
    if message == 'left_click':
        mouse.left_click()
    elif message == 'right_click':
        mouse.right_click()
    
    # scrolling
    elif message == 'scroll_down':
        mouse.scroll(0, 1)
    elif  message == 'scroll_up':
        mouse.scroll(0, -1)
    
    # mouse movement
    elif message.contains('move'):
        x = message.split('_')[1] * screen_width
        y = message.split('_')[2] * screen_height
    
    # error case
    else:
        print ('Invalid message - packet ignored')