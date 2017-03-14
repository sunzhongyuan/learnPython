list1 = ['1.aaa','2.bbb','3.ccc','4.ddd']
list2 = ['4.444','2.222','3.333','1.111']
list3 = []
for x in list1:
    for y in list2:
        if x[0] == y[0]:
            list3.append(x+':'+(y[2:]));

print(list3)
