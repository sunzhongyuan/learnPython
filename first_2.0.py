import random
print("--------------------游戏？？-------------------")
i = 0
ans = random.randint(1,10)
while i < 10:
    i = i + 1
    temp = input("请猜一个数字:")
    while temp.isdigit() == False:
        temp = input("输入错误！！请输入数字:")
    guess = int(temp)
    if guess == ans:
        print("猜中了！！")
        break
    else:
        print("猜错了")
        if guess > ans:
            print("提示：大了")
            continue
        else:
            print("提示：小了")
            continue
print("答案是:",ans)
print("游戏结束")
