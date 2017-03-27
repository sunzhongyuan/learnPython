class MyDes:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.val

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.val = value

    def __delete__(self, instance):
        print("正在删除变量：", self.name)
        print("噢~这个变量没法删除~")

class Test:
    n = '123'
    a = MyDes(n,'n')
    

t = Test()
t.a
t.a = '345'
