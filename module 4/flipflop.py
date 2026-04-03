def palind(r):
    end = len(r)-1
    start = 0
    while (start < end):
        if (r[start] != r[end]):
            return False
        start += 1
        end -= 1
    return True


r = (1, 2, 3, 4, 4, 4, 4, 3, 2, 2)

if palind(r):
    print("the tupple is flipflop")

else:
    print("the tupple is not flipflop")
