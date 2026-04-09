class IOstring:

    def __init__(self):
        self.str1 = ""

    def __getstring__(self):
        self.str1 = input("please enter a string: ")

    def print(self):
        print("Result is ", self.str1.upper())


str1 = IOstring()

str1.__getstring__()
str1.print()
