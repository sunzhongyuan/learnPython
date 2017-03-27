class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(self.values,0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[self.values[key]] += 1
        return self.values[key]

    def __setitem__(self,key,value):
        self.values[key] = value

    def __delitem__(self,key):
        del self.count[self.values[key]]
        del self.values[key]

    def append(self,value):
        self.values.append(value)
        self.count[value] = 0

    def pop(self,index):
        self.count.pop(self.values[index])
        self.values.pop(index)
        
    def remove(self,value):
        del self.count[value]
        self.values.remove(value)

    def insert(self,index,value):
        self.values.insert(index,value)
        self.count[value] = 0
    
    def clear(self):
        self.values.clear()
        self.count.clear()

    def reverse(self):
        self.values.reverse()

    def counter(self,index):
        return self.count[self.values[index]]
