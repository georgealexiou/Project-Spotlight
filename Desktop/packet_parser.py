from cursor import Cursor
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


class Parser:

    def __init__(self):
        self.cursor = Cursor()

    def receive_message(self, message):
        self.parse(message.split(":")[0], message.split(":")[1])

    def parse(self, key, value):

        # clicks
        if key == 'Cursor_Right':
            if value == 'Click':
                self.cursor.right_click()
        elif key == 'Cursor_Left':
            if value == 'Click':
                self.cursor.left_click()
            
        # scrolling
        #TODO: may have to change this to support faster scrolling
        elif key == 'Cursor_Scroll':
            if value == 'Down':
                self.cursor.scroll(0, -500)
            elif value == 'Up':
                self.cursor.scroll(0, 500)
            
        # cursor movement
        elif key == 'Cursor_Move':
            x = int(float(value.split(',')[0]) * screen_width)
            y = int(float(value.split(',')[1]) * screen_height)

            self.cursor.set_position(x,y)
        
        # Shutting down case.
        else:
            self.cursor.cursor_reset()

#parser = Parser()
#parser.receive_message("Cursor_Move:0.5,0.2")