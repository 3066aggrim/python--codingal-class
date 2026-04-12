class Nepal():
    def capital(self):
        print("Kathmandu is our capital")

    def language(self):
        print("we speak nepali also known as khas bhasa")

    def type(self):
        print("Nepal will be a developing country because of BALEN!")


class India():
    def capital(self):
        print("New ddelhi is our capital")

    def language(self):
        print("we speak hindi,urdu tamil,malyalam and many more")

    def type(self):
        print("India is a developing country")


obj_nep = Nepal()
obj_ind = India()

for country in (obj_nep, obj_ind):
    country.capital()
    country.language()
    country.type()
