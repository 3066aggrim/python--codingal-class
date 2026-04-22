from tkinter import *

window = Tk()
window.title("Event Handling")
window.geometry("100x100")


def handle_keypress(event):
    """Print the char associated to the key pressed"""
    print(event.char)


window.bind("<Key>", handle_keypress)


def handle_click(event):
    print("button was clicked")


button = Button(window, text="Click me")

button.pack()

button.bind("<Button-1>", handle_click)
window.mainloop()
