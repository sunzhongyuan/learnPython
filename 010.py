member = ['a','b','c','d', 'e']
number = [88, 90, 85, 90, 88]
index = 1
for i in number:
    member.insert(index,i)
    index += 2
print(member)

for j in member:
    if isinstance(j,str):
        print(j, end=' ')
    else:
        print(j)


#方法一：
count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2

#方法二：    
    
for each in range(len(member)):
    if each%2 == 0:
        print(member[each], member[each+1])
