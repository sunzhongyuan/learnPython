
def fun1():
    file_name = input('请输入文件名：')
    file = open(file_name, 'x')
    print("请输入内容【单独输入':w'保存退出】：")
    while 1:
        file_content = input()
        if file_content == ':w':
            file.close()
            return
        file.write(file_content+'\n')

#fun1()


def fun2():
    file_name1 = input('请输入文件名1：')
    file_name2 = input('请输入文件名2：')

    file1 = open(file_name1)
    file2 = open(file_name2)

    x = len(list(file1))
    y = len(list(file2))
    file1.seek(0,0)
    file2.seek(0,0)

    count = 0

    for i in range( x if x > y else y):
        if file1.readline() != file2.readline():
            print('第 %d 行不一样' % (int(i)+1) )
            count += 1

    print('两个文件共有 %d 处不同' % count)

    file1.close()
    file2.close()

#fun2()


def fun3():
    file_name = input('请输入需要打开的文件：')
    file = open(file_name)
    line_num = int(input('请输入需要显示的该文件前几行：'))
    count = 0
    for each_line in file:
        count += 1
        if count > line_num:
            break
        print(each_line.replace('\n',''))
    file.close()

#fun3()


def fun4():
    file_name = input('请输入需要打开的文件：')
    file = open(file_name)
    line_num = input('请输入需要显示的行数【例如 13:21 :21 21:】：')

    list_num = line_num.split(':')
    
    if list_num[0] == '':
        list_num[0] = 0
    else:
        list_num[0] = int(list_num[0])

    count = 0
    for each_line in file:
        count += 1
        if list_num[0] <= count and (list_num[1] == '' or int(list_num[1]) >= count):
            print(each_line.replace('\n',''))
    file.close()   

#fun4()


def fun5():
    file_name = input('请输入需要打开的文件：')
    file = open(file_name)
    old_str = input('请输入需要替换的单词或字符：')
    new_str = input('请输入新的单词或字符：')
    file_content = file.read()
    count = file_content.count(old_str)
    print('\n 文件 %s 中共有%d个【%s】' % (file_name,count,old_str))
    print('您确定要把所有的【%s】替换为【%s】吗' % (old_str,new_str))

    flag = (input('【YES/NO】:')).upper()

    if flag == 'YES':
        file_content = file_content.replace(old_str,new_str)
        file2 = open(file_name,'w')
        file2.write(file_content)
        file2.close()
        print('修改成功')
    else:
        print('不修改')
    file.close()

fun5()
    
    
