def parser():
    txt = "Right_Click:1,2"

    inputText = txt.partition(":")

    if inputText[0] == "Mouse_Coordinates":
        cOord = inputText[2].partition(",")
        mouse_display(cOord[0], cOord[2])
    elif inputText[0] == "Scroll":
        cOord = inputText[2].partition(",")
        scroll(0, cOord[2])
    elif inputText[0] == "Left_Click":
        left_click()
    elif inputText[0] == "Right_Click":
        right_click()
    else:
        print("Wrong input")


def mouse_display(x, y):
    print(x, y)

def left_click():
    print("Left click")

def right_click():
    print("Right click")

def scroll(x, y):
    print(x, y)

parser()
