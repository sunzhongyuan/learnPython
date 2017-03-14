def MyFunction(*params, base=3):
    sum = 0
    for i in params:
        sum += i
    return (sum * base)

print(MyFunction(1,1,3))
print(MyFunction(1,1,3,base=5))



for num in range(100,999):
    num1 = 0
    for i in str(num):
        num1 += int(i)*int(i)*int(i)
    if num == num1:
        print(num)
                        

string = input('请输入目标字符串：')
string1 = input('请输入子字符串(两个字符)：')
print('子字符串在目标字符串中共出现',string.count(string1),'次')
