test_dict = {'codingal': 2, 'is': 2, 'best': 5, 'worst': 2}
print("original dict is ", test_dict)

A = int(input("please enter a number"))
res = 0
for key in test_dict:
    if test_dict[key] == A:
        res = res+1

print('result is ', res)
