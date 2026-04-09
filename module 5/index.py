class pair_element:

    def twosums(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num], i)
            lookup[num] = i


value = int(input("enter a number: "))
print("index1=%d, index23=%d " % pair_element().twosums(
    (10, 20, 30, 40, 50, 60, 70, 80, 90), value))
