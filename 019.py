def isHL():
    string = input('请输入一句话：')
    for each in range(0,len(string)//2):
        if string[each] != string[len(string)-each-1]:
            return '不是回联'
    return '是回联'
    
print(isHL())


def CountFunc(*params):
    paraNum = 0
    for string in params:
        strCount = 0
        numCount = 0
        spaCount = 0
        othCount = 0
        for each in string:
            if each.isalpha():
                strCount += 1
            elif each.isdigit():
                numCount += 1
            elif each.isspace():
                spaCount += 1
            else:
                othCount += 1
        paraNum += 1
        print('第',paraNum,'个字符共有：英文字母',strCount,'个，数字',numCount,'个，空格',spaCount,'个，其他字符',othCount,'个。')

CountFunc('I love fishc.com.', 'I love you you love me.', '1q2  w3&^%e4 r<>')
