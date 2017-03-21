import os

def fun1():
    '统计当前目录下每个文件类型的文件数，包括文件夹数'
    dir_info = {}
    listdir = os.listdir(path = '.')
    for each in listdir:
        if os.path.isdir(each):
            extension = '文件夹'
        else:
            (name,extension) = os.path.splitext(each)
            
        if extension in dir_info:
            dir_info[extension] = dir_info[extension] + 1
        else:
            dir_info[extension] = 1

    for each in list(dir_info.keys()):
        print('该文件夹下共有类型为【%s】的文件%d个' % (each,dir_info[each]))

#fun1()


def fun2():
    '计算当前文件夹下所有文件的大小'
    info_dir = {}
    list_dir = os.listdir(path = '.')

    for each in list_dir:
        if os.path.isfile(each):
            info_dir[each] = os.path.getsize(each)

    for each in list(info_dir.keys()):
        print(each,'【%dBytes】' % info_dir[each])

#fun2()


def fun3(path):
    '搜索指定文件夹包括子文件夹下所有视频文件，并将视频文件路径写入filelist.txt文件'
    result_file = path+'\\filelist.txt'
    f = open(result_file, 'w')
    
    file_list = list(os.walk(path))
    for each_tuple in file_list:
        for file in each_tuple[2]:
            file_path = each_tuple[0] + '\\' + file
            file_type = list(os.path.splitext(file))[1]
            if file_type in ('.mp4','.avi','.rmvb'):
                print(file_path)
                f.write(file_path + '\n\n')
    print('结果已写入文件：' + result_file)
    f.close()

#fun3('c:\\test')
        


def fun4(path,keyWord):
    '查找指定文件夹包括子文件夹中所有txt文档包含关键字的文件，并打印关键字出现的位置'
    file_list = list(os.walk(path))
    for each_tuple in file_list:
        for file in each_tuple[2]:
            file_path = each_tuple[0] + '\\' + file     #文件路径
            file_type = list(os.path.splitext(file))[1]     #文件扩展名
            if file_type == '.txt':
                f = open(file_path)
                line_num = 0        #行数计数器
                index_dict = {}     #字典 存储当前文件查找结果
                for each in f:
                    line_num += 1       #当前文件第几行
                    index_list = []     #位置列表

                    index_num = each.find(keyWord)      #在当前行找一下看有没有关键字
                    while index_num != -1:              #当前行有关键字
                        index_num += 1                  #指针位置后移一位
                        index_list.append(index_num)    #记下关键字位置
                        index_num = each.find(keyWord,index_num)  #继续找

                    #如果当前行有关键字 把当前行的结果放到字典里
                    if len(index_list) != 0:
                        index_dict[line_num] = index_list
                    
                #当前文件所有行都找完了  结果字典里有值就输出
                if len(index_dict) != 0:
                    print('======================================================')
                    print('在文件【%s】中找到关键字【%s】' % (file_path,keyWord))
                    for each in index_dict.keys():
                        print('关键字出现在第',each,'行，第',index_dict[each],'个位置')
                f.close()



fun4('c:\\test', 'aaa')










    
