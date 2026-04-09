class dog:
    species = "animal"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


Lucky = dog("lucky", 8, 'husky')
Pintu = dog("Pintu", 7, 'stray')

print("lucky  is an {}".format(Lucky.species))
print("blu's is an {}".format(Pintu.species))

print("{} is {} years old is a {}".format(Lucky.name, Lucky.age, Lucky.breed))
print("{} is {} years old is a {}".format(Pintu.name, Pintu.age, Pintu.breed))
