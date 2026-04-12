class Reverse:

    def __init__(self, text):
        self.text = text

    def show(self):
        words = self.text.split()
        words.reverse()
        print(" ".join(words))


s = Reverse("I love Python")


s.show()
