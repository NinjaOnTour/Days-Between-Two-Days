import math

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def printDate(self):
        print(f"{self.day}/{self.month}/{self.year}")

def distance(d0, d1): # this function is not completely correct
    day = abs(d0.day - d1.day)
    month = abs(d0.month - d1.month)
    year = abs(d0.year - d1.year)
    bonus = 0 # there is 1 bonus day per 4 year
    for i in range(d0.year, d1.year):
        if i % 4 == 0:
            bonus += 1
    if d1.year % 4 == 0 and d1.month > 2:
        bonus += 1
    return (year-1)*365 + ((12-d0.month)+(d1.month))*30 + day + bonus

date0 = Date(9, 11, 2022)
date1 = Date(11, 3, 2024)
date0.printDate()
date1.printDate()
print(f"distance = {distance(date0, date1)}")
