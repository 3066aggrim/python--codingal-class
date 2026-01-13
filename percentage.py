# take marks as input from user

print("Enter Marks Obtained in 4 Subjects: ")

math = int(input("maths :"))

english = int(input("english :"))

science = int(input("science :"))

nepali = int(input("nepali :"))

# Let's calculate the percentage of marks

sum = math + english + science + nepali

print("sum of math,english,science and nepali:", sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")

print(perc)
86
