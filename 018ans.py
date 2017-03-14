def mFun(*param, base=3):
    result = 0
    for each in param:
        result += each

    result *= base
    
    print('结果是：', result)

mFun(1, 2, 3, 4, 5, base=5)


def Narcissus():
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp%10) ** 3
            temp = temp // 10  # 注意这里用地板除

        if sum == each:
            print(each, end='\t')

print("所有的水仙花数分别是：", end='')
Narcissus()


def findStr(desStr, subStr):
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串!')
    else:
        for each1 in range(length-1):      
            if desStr[each1] == subStr[0]:
                if desStr[each1+1] == subStr[1]:
                    count += 1
                    
        print('子字符串在目标字符串中共出现 %d 次' % count)

desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串(两个字符)：')
findStr(desStr, subStr)
