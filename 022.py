def fun1(num):
    result = num
    for i in range(1,num):
        result *= i
    print(result)

fun1(5)



def fun2(num):
    if num == 1:
        return 1
    else:
        return num * fun2(num-1)

print(fun2(5))



def fun3(x,y):
    if y == 1:
        return x
    else:
        return x*fun3(x,y-1)

print(fun3(3,4))


#ans

def power(x, y):
    if y:
        return x * power(x, y-1)
    else:
        return 1
    
print(power(2, 3))


#返回x和y的最大公约数
def gcd(x, y):
    if y:
        return gcd(y, x%y)
    else:
        return x
    
print(gcd(4, 6))
