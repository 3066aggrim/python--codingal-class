weight = float(input("insert your weight in kg"))
height = float(input("insert your height in cm"))

BMI = weight/(height/100)**2
print("your BMI is", BMI)

if BMI <= 18.4:
    print("youre under weight")

elif BMI <= 24.9:
    print("youre healthy")

elif BMI <= 29.9:
    print("youre overweight")

elif BMI <= 34.9:
    print("you are severy overweight")

elif BMI <= 39.9:
    print("you are obese")

else:
    print("you are severy obese")
