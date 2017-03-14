number = '1234567890'
string1 = 'abcdefghijklmnopqrstuvwxyz'
string2 = string1 + string1.upper()
string3 = '~!@#$%^&*()_+-/,.?<>;:[]{}|\\'

errMsg = '''请按以下方式提上您的密码安全级别：
        1.密码必须由数字/字母及特殊字符三种组合
        2.密码只能由字母开头
        3.密码长度不能低于16位'''

password = input('请输入需要检查的密码组合：')
if (len(password) <= 8) or password.isdigit() or password.isalpha():
    print('你的密码安全级别评定为：低')
    print(errMsg)
elif (len(password) > 16) and password[0].isalpha():
    for num in number:
        if num in password:
            numFlag = 1
            break
        numFlag = 0
    for str2 in string2:
        if str2 in password:
            str2Flag = 1
            break
        str2Flag = 0
    for str3 in string3:
        if str3 in password:
            str3Flag = 1
            break
        str3Flag = 0
    print('numFlag',numFlag,'str2Flag',str2Flag,'str3Flag',str3Flag)
    if  numFlag and str2Flag and str3Flag:
        print('你的密码安全级别评定为：高')
        print('请继续保持')
    else:
        print('你的密码安全级别评定为：中')
        print(errMsg)
else:
    print('你的密码安全级别评定为：中')
    print(errMsg)
