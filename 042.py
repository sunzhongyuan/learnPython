class Nstr(str):
    def __sub__(self,other):
        index = 0
        for each in self:
            if each in other:
                self = self[:index] + self[index+1:]
                continue
            index += 1

        return self


class Nstr1(str):
    def __sub__(self, other):
        return self.replace(other, '')


