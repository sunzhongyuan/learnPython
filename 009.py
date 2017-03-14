i = 3
ans = input("请输入密码：")
while True:
    if '*' in ans:
        temp = '密码中不能包含"*"号！你还有',i,'次机会！请输入密码：'
        ans = input(temp)
        continue
    
    i -= 1
              
    if '1218' != ans:
        if i < 1:
            print('密码输入错误！没有机会了！')
            break
        else:
            temp = '密码输入错误！您还有',i,'次机会！请输入密码：'
            ans = input(temp)
            continue
    else:
        print('密码正确！进入程序。。。')
        break
