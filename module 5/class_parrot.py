class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = parrot("blu", 3)
woo = parrot("woo", 5)

print("woo's  is a {}".format(woo.species))
print("blu's is a {}".format(blu.species))

print("{} is {} years old".format(woo.name, woo.age))
print("{} is {} years old".format(blu.name, blu.age))
