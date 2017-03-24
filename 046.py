class Celsius:
    def __init__(self,value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) /1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()



class DescA():
    def __get__(self,obj,type=None):
        print("Aget")

    def __set__(self,obj,val):
        obj.a = val
        print('Aset')

class DescB():
    def __get__(self,obj,type=None):
        print("Bget")

class A():
    x = DescA()
    y = DescB()
    def __init__(self,x,y):
        self.x = x
        self.y = y

'''
>>> a = A(2,3)
Aset
>>> a.__dict__
{'a': 2, 'y': 3}
>>> a.x
Aget
>>> a.y
3
>>> 
'''
