
class Ticket:
    price = 100
    child = 50

    def setWeek(self,week):
        if week in ('Weekend','Saturday','Sunday'):
            self.price = self.price * 1.2
            self.child = self.price * 0.5

    def getPrice(self,men,child):
        return men*self.price + child*self.child




class Ticket():
        def __init__(self, weekend=False, child=False):
                self.exp = 100
                if weekend:
                        self.inc = 1.2
                else:
                        self.inc = 1
                if child:
                        self.discount = 0.5
                else:
                        self.discount = 1
        def calcPrice(self, num):
                return self.exp * self.inc * self.discount * num

>>> adult = Ticket()
>>> child = Ticket(child=True)
>>> print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))
2个成人 + 1个小孩平日票价为：250.00
