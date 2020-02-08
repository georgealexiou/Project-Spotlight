def parser():
    txt = "Mouse_Coordinates:1,2"

    inputText = txt.partition(":")

    print(inputText[2])

    if inputText[2] == "Mouse_Coordinates":
        cOord = inputText[2].partition(",")
        mouse_display(cOord[1], cOord[2])
    elif inputText[2] == "Scroll":
        cOord = inputText[2].partition(",")
        scroll(0, cOord[2])
    elif inputText[2] == "Pressed_Down":
        pressed_down()
    elif inputText[2] == "Released":
        release()


def mouse_display(x, y):
    print(x, y)


def scroll(x, y):
    print(x, y)


def pressed_down():
    print("Pressed down")


def release():
    print("Released")

parser()
