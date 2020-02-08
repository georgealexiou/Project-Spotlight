import mouse.py as Mouse
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

mouse = Mouse.Mouse()

def parse(message):
        
    key = message.split(":")[0]
    value = message.split(":")[1]

    try
        # clicks
        if key == 'Mouse_Right':
            if value == 'Click':
                mouse.right_click()
        elif message == 'Mouse_Left':
            if value == 'Click':
                mouse.left_click()
        
        # scrolling
        #TODO: may have to change this to support faster scrolling
        elif message == 'scroll_down':
            mouse.scroll(0, 1)
        elif  message == 'scroll_up':
            mouse.scroll(0, -1)
        
        # mouse movement
        elif message.contains('Mouse_Coordinates'):
            x = message.split(':')[1].split * screen_width
            y = message.split('_')[2] * screen_height
        
        # error case
        else:
            print ('Invalid message - packet ignored')