>>> class C:
        def __getattr__(self, name):
                print(1)
                return super().__getattr__(name)
        def __getattribute__(self, name):
                print(2)
                return super().__getattribute__(name)
        def __setattr__(self, name, value):
                print(3)
                super().__setattr__(name, value)
        def __delattr__(self, name):
                print(4)
                super().__delattr__(name)

                
>>> c = C()
>>> c.x
2
1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c.x
  File "<pyshell#29>", line 4, in __getattr__
    return super().__getattr__(name)
AttributeError: 'super' object has no attribute '__getattr__'



class Counter:
        def __init__(self):
                self.counter = 0 # 这里会触发 __setattr__ 调用
        def __setattr__(self, name, value):
                self.counter += 1
'''既然需要 __setattr__ 调用后才能真正设置 self.counter 的值，所以这时候 self.counter 还没有定义，所以没法 += 1，错误的根源。'''
                super().__setattr__(name, value)
        def __delattr__(self, name):
                self.counter -= 1
                super().__delattr__(name)



class Counter:
        def __init__(self):
                super().__setattr__('counter', 0)
        def __setattr__(self, name, value):
                super().__setattr__('counter', self.counter + 1)
                super().__setattr__(name, value)
        def __delattr__(self, name):
                super().__setattr__('counter', self.counter - 1)
                super().__delattr__(name)
