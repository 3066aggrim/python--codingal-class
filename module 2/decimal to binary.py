decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)[2:]  # remove the '0b' prefix

print("Binary equivalent:", binary)
