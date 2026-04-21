from tkinter import *

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

lbl1 = Label(text="full name", bg="#0E7BC4")
lbl2 = Label(text="email id", bg="#0E7BC4")
lbl3 = Label(text="enter password", bg="#0E7BC4")

name_entry = Entry()
email_entry = Entry()
pass_entry = Entry(show="*")


def display():
    name = name_entry.get()
    greet = "hey"+name
    message = "\nCongrats for your new account"
    textbox.insert(END, greet)
    textbox.insert(END, message)


textbox = Text(bg="#FFFFFF", fg="black")

btn = Button(text="create Account", command=display)

lbl1.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
pass_entry.pack()
btn.pack()
textbox.pack()

root.mainloop()
