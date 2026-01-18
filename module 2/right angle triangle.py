print("Half pyramid pattern of stars")
rows = int(input("please enter the rows you want"))

for i in range(rows):
    for j in range(i+1):
        print("*  ", end="")
    print()
