class RomanConverter:

    def __init__(self):
        # Dictionary for Roman values
        self.roman_dict = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }

    def int_to_roman(self, num):
        roman = ""

        for value in sorted(self.roman_dict.keys(), reverse=True):
            while num >= value:
                roman += self.roman_dict[value]
                num -= value

        return roman


converter = RomanConverter()

number = int(input("Enter a number: "))

print("Roman numeral is:", converter.int_to_roman(number))
