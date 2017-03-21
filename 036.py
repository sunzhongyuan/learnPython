
class Person:
    name = '小甲鱼'

    def setName(self,name):
        self.name = name

    def getName(self):
        print(self.name)
        

pp = Person()
pp.getName()
pp.setName('aaa')
pp.getName()



class Rectangle:
    high = 5.00
    width = 4.00

    def setRect(self):
        self.high = float(input('请输入矩形的长和宽...\n长：'))
        self.width = float(input('宽：'))

    def getRect(self):
        print('这个矩形的长是：%.2f，宽是：%.2f' % (self.high,self.width))

    def getArea(self):
        print(self.high * self.width)
        
    
