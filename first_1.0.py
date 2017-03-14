import random
print("--------------------游戏？？-------------------")
i = 0
ans = random.randint(1,10)
while i < 10:
    i = i + 1
    temp = input("请在心里猜一个数字:")
    guess = int(temp)
    if guess == ans:
        print("猜中了！！")
        break
    else:
        if guess > ans:
            print("大了")
            continue
        else:
            print("小了")
            continue
print("答案是:",ans)
print("游戏结束")
