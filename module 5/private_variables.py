class myclass:

    __privatevar = 22

    def __privateMeth(self):
        print("i am inside my class")

    def hello(self):
        print("private variable value", myclass.__privatevar)


foo = myclass()
foo.hello()
foo.__privateMeth
