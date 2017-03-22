
class MyClass1:
    count = 0

    def __init__(self):
        MyClass1.count += 1

    def delete(self):
        MyClass1.count -= 1

    def printCount(self):
        print(MyClass1.count)


class C:
    count = 0
        
    def __init__(self):
            C.count += 1

    def __del__(self):
            C.count -= 1


class Stack:
    list_data = list()

    def isEmpty(self):
        return len(self.list_data) == 0

    def push(self,data):
        self.list_data.append(data)

    def pop(self):
        self.list_data.pop()

    def top(self):
        return self.list_data[len(self.list_data) - 1]

    def bottom(self):
        return self.list_data[0]


class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty(self):
        return not self.stack
    
    def push(self, obj):
        self.stack.append(obj)
 
    def pop(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack.pop()
 
    def top(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[-1]
 
    def bottom(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[0]
