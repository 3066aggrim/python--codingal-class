numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [1, 3, 4, 2, 5]
result = map(lambda x, y: x+y, numbers_1, numbers_2)
print("adittion of two lists")
print(list(result))

nums = [1, 2, 3, 4, 5]


def sq(n):
    return n*n


square = list(map(sq, nums))
print("Square of numbers in list")
print(square)
