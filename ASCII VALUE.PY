character = input("enter a single character")

if type(character) is str and len(character) == 1:
    print("valid input")

else:
    print("invalid input")

ascii_value = ord(character)
print(f"Character:  {character}")
print(f"ASCII Value: {ascii_value}")

if ascii_value >= 65 and ascii_value <= 90:
    print("Type: Uppercase letter")

elif ascii_value >= 97 and ascii_value <= 122:
    print("type: lowercase letter")

elif ascii_value > 48 and ascii_value <= 57:
    print("type:digit")

elif ascii_value == 32:
    print("type: space")

else:
    print("type: special character")
