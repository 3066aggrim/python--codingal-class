numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33,]
user_value = int(input("Enter a number: "))

odd_numbers = []

for num in numbers:
    if num % 2 != 0 and num < user_value:
        odd_numbers.append(num)

print("Odd numbers below input:", odd_numbers)
