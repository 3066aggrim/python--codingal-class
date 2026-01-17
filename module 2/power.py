n = int(input("enter a number"))
power = int(input("enter a power"))
ans = 1
for i in range(1, power + 1):
    ans = ans * n
print(ans)
