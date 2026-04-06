x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])

print("x:", x)
print("y:", y)

print("isdisjoint()", x.isdisjoint(y))
print("difference()", y.difference(x))

print("x|y:", x | y)
