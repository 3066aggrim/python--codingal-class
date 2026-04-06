s1 = {2, 3, 1}
s2 = {'b', 'c', 'a'}
s3 = list(zip(s1, s2))
print(s3)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


stock = ['meroshare', 'reliance', 'tcs']
prices = [2000, 2500, 1750]

new_dict = {stock: prices for stock, prices in zip(stock, prices)}
print('\n{}'.format(new_dict))
