from cursor import Cursor
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


class Parser:

    def __init__(self):
        pass

    def receive_message(self, message):
        self.parse(message.split(":")[0], message.split(":")[1])

    def parse(self, key, value):

        # clicks
        if key == 'Cursor_Right':
            if value == 'Click':
                cursor.right_click()
        elif message == 'Cursor_Left':
            if value == 'Click':
                cursor.left_click()
            
        # scrolling
        #TODO: may have to change this to support faster scrolling
        elif key == 'Cursor_Scroll':
            if value == 'Down':
                cursor.scroll(0, 1)
            elif value == 'Up':
                cursor.scroll(0, -1)
            
        # cursor movement
        elif key == 'Cursor_Move':
            x = int(float(value.split(',')[0]) * screen_width)
            y = int(float(message.split(',')[1]) * screen_height)

            cursor.set_position(x,y)
        
        # error case
        else:
            print ('Invalid message - packet ignored')