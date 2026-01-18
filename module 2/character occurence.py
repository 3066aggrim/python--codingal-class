word = input("please enter a word")
char = input("please enter a single character")

i = 0
count = 0

while i < len(word):

    if (word[i] == char):
        count = count+1

    i = i+1
print("the totel number of times", char, "has occured=", count)
