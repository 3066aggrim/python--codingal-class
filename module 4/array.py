import array as arr

array_num = arr.array('i', [1, 3, 4, 6, 8, 4, 9])
print("original array :"+str(array_num))
print('Number of occurences of the number 3 in the said array:' +
      str(array_num.count(4)))

array_num.reverse()
print("reverse the order of the items:")
print(str(array_num))
