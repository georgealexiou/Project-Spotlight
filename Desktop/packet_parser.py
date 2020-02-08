import mouse.py as Mouse
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

mouse = Mouse.Mouse()

def parse(message):
        
    key = message.split(":")[0]
    value = message.split(":")[1]

    # clicks
    if key == 'Mouse_Right':
        if value == 'Click':
            mouse.right_click()
    elif message == 'Mouse_Left':
        if value == 'Click':
            mouse.left_click()
        
    # scrolling
    #TODO: may have to change this to support faster scrolling
    elif key == 'Mouse_Scroll':
        if value == 'Down':
            mouse.scroll(0, 1)
        elif value == 'Up':
            mouse.scroll(0, -1)
        
    # mouse movement
    elif key == 'Mouse_Move':
        x = value.split(',')[0].split * screen_width
        y = message.split(',')[1] * screen_height
    
    # error case
    else:
        print ('Invalid message - packet ignored')