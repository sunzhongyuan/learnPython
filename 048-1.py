alist = range(5)
it = iter(alist)

while True:
    try:
        print(next(it))
    except StopIteration:
        break


import datetime as dt

class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapYear(self, year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False
        
    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1 

        temp = self.now
        self.now -= 1
        
        return temp


class MyRev:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.data[self.index]
