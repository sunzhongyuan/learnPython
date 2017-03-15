def palindrome(string):
    length = len(string)
    last = length-1
    length //= 2
    flag = 1
    for each in range(length):
        if string[each] != string[last]:
            flag = 0
        last -= 1

    if flag == 1:
        return 1
    else:
        return 0

string = input('请输入一句话：')
if palindrome(string) == 1:
    print('是回文联!')
else:
    print('不是回文联！')


def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文联!'
    else:
        return '不是回文联！'
print(palindrome('上海自来水来自海上'))


def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i+1, letters, digit, space, others))
            
count('I love fishc.com.', 'I love you, you love me.')
