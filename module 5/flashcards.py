class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+'('+self.meaning+')'


flash = []
print("welcome to flashcard application")


while (True):
    word = input("please enter your word you want to add:")
    meaning = input("please enter the meaning of your word:")

    flash.append(flashcards(word, meaning))
    option = int(input("do you want to continue it? 1 for no 0 for yes:"))

    if (option):
        break
print("Your flashcards")
for i in flash:
    print("=>", i)
