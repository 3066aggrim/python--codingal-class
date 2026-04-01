import random
import time


def getrandomDate(starDate, endDate):

    print("printing random date between", starDate, "and", endDate)

    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(starDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = starttime+randomGenerator * (endtime - starttime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate


print("Random date =", getrandomDate("1/1/2020", "12/12/2024"))
