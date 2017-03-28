i = 0
while i in range(5):
    print(i)
    i += 1

    
class LeapYear:
    def __init__(self):
        self.year = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.year += 1
            if (self.year%4 == 0 and self.year%100 != 0) or self.year%400 == 0 :
                if self.year > 2017:
                    raise StopIteration
                return self.year


class MyTev:
    def __init__(self,para):
        self.para = para
        self.len = len(para)
    def __iter__(self):
        return self
    def __next__(self):
        self.len -= 1
        if self.len < 0:
            raise StopIteration
        else:
            return self.para[self.len]
