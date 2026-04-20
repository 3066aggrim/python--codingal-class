from tkinter import *
from datetime import date

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

lbl = Label(text="hey there!", fg="white", bg="#3b6cff")

name_lbl = Label(text="full name", bg="#152c71")
name_entry = Entry()


def display():

    name = name_entry.get()

    global message
    message = "welcome to the application!\ntoday's date"
    greet = "hello"+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())


text_box = Text(height=3)

btn = Button(text="begin", command=display, height=1, bg="#1261A0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()
