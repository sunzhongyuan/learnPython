point = '''
|--- 新建用户：N/n ---|
|--- 修改密码：U/u ---|
|--- 登陆账户：E/e ---|
|--- 删除账户：D/d ---|
|--- 退出程序：Q/q ---|'''

dicts = dict()
print(point)

while 1:
    command = (input('|--- 请输入指令代码：')).upper()

    if command == 'N':
        name = input('请输入用户名：')
        while name in dicts:
            name = input('此用户名已经被使用，请重新输入：')
        pwd = input('请输入密码：')
        dicts[name] = pwd
        print('注册成功，赶紧试试登陆吧。。。')
    elif command == 'U':
        name = input('请输入用户名：')
        while (name in dicts) == False:
            name = input('您输入的用户名不存在，请重新输入：')
        pwdOld = input('请输入旧密码：')
        while dicts[name] != pwdOld:
            pwdOld = input('旧密码错误，请重新输入：')
        pwd = input('请输入新密码:')
        dicts[name] = pwd
        print('修改成功，赶紧试试登陆吧。。。')
    elif command == 'E':
        name = input('请输入用户名：')
        while (name in dicts) == False:
            name = input('您输入的用户名不存在，请重新输入：')
        pwdOld = input('请输入密码：')
        while dicts[name] != pwdOld:
            pwdOld = input('密码错误，请重新输入：')
        print('登陆成功！！！')
    elif command == 'D':
        name = input('请输入用户名：')
        while (name in dicts) == False:
            name = input('您输入的用户名不存在，请重新输入：')
        pwdOld = input('请输入密码：')
        while dicts[name] != pwdOld:
            pwdOld = input('密码错误，请重新输入：')
        dicts.pop(name)
        print('删除成功！！！')
    elif command == 'Q':
        print('退出成功')
        break
    else:
        print('指令错误！')


    
