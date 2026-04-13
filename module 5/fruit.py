import random


class fruitQuiz:
    def __init__(self):

        self.fruits = {'apple': 'red',
                       'bananna': 'yellow',
                       'peach': 'skin colour',
                       'orange': 'orange',
                       'watermelon': 'green', }

    def quiz(self):
        while (True):

            fruit, colour = random.choice(list(self.fruits.items()))

            print("what is the color of{}".format(fruit))
            user_answer = input()

            if (user_answer.lower() == colour):
                print("correct answer")

            else:
                print("wrong answer")

            option = int(input("enter 0 for continuation or 1 to stop it:"))
            if (option):
                break


print("welcome to fruit quiz")
fq = fruitQuiz()
fq.quiz()
