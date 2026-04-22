from tkinter import *


def multiply():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result.set(num1 * num2)
    except:
        result.set("Invalid input")


root = Tk()
root.title("Multiply Two Numbers")
root.geometry("300x200")

result = StringVar()

Button(root, text="Enter first number").pack()
entry1 = Entry(root)
entry1.pack()

Button(root, text="Enter second number").pack()
entry2 = Entry(root)
entry2.pack()

Button(root, text="Multiply", command=multiply).pack(pady=10)
Label(root, text="Result:").pack()
Label(root, textvariable=result).pack()

root.mainloop()
