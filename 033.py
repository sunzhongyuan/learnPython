#try-except语句
#可以捕获具体异常 推荐
try:
    sum = 1 + '1'
    f = open('aaa.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错:' + str(reason))
except TypeError as reason:
    print('类型出错:' + str(reason))

try:
    sum = 1 + '1'
    f = open('aaa.txt')
    print(f.read())
    f.close()
except (OSError,TypeError):
    print('出错')

#也可以捕获全部异常 不推荐
try:
    sum = 1 + '1'
    f = open('aaa.txt')
    print(f.read())
    f.close()
except:
    print('出错')



#try-finally语句
#finally里的语句无论如何都会被执行
try:
    f = open('aaa.txt','w')
    f.write('12111212')
    sum = 1 + '1'
except (OSError,TypeError):
    print('出错')
finally:
    f.close()

raise 自定义异常说明
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> raise ZeroDivisionError('除数不能为零')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    raise ZeroDivisionError('除数不能为零')
ZeroDivisionError: 除数不能为零
>>>
