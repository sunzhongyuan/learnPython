result1 = 0
result2 = 0
result3 = 0
for i in range(1,13):
    if i <= 2:
        result1 = 1
        result2 = 1
    else:
        result3 = result1 + result2
        result1 = result2
        result2 = result3
        

print(result2)
        
        


def fun(x):
    if x <= 2:
        return 1
    else:
        return fun(x-1) + fun(x-2)


print(fun(12))



def fun1(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        fun1(n-1,x,z,y)
        print(x ,'-->',z)
        fun1(n-1,y,x,z)

fun1(4,'1','2','3')    



def fun2(x):
    if x == 1:
        return 10
    else:
        return 2+fun2(x-1)

print(fun2(5))

             
        
