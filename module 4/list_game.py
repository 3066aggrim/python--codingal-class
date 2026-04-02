L = [1, 3, 4, 6, 8, 7, 0, 3]
print("original list:", L)

sum = 0
for i in L:
    sum += i

avg = sum/len(L)

print("sum=", sum)

print("average=", avg)

L.sort()
print("sorted list:", L)

print("smallest element is", L[0])

print("largest element is:", L[-1])
