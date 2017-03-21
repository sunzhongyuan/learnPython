#raise应用
try:
    for i in range(3):
        for j in range(3):
            if i == 2:
                raise KeyboardInterrupt
            print(i, j)
except KeyboardInterrupt:
    print('退出啦！')


#异常可以提示用户操作错误
def int_input(prompt=''):
    while True:
        try:
            int(input(prompt))
            break
        except ValueError:
            print('出错，您输入的不是整数！')

int_input('请输入一个整数：')


#打开失败 执行close()出错问题  
try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    if 'f' in locals(): # 如果文件对象变量存在当前局部变量符号表的话，说明打开成功
        f.close()
