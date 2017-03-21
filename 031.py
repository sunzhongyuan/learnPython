import pickle

file = open('C:\\python\\record.txt', 'r')
list_boy = []
list_girl = []
num = 0

for each_line in file:
    if each_line[:3] == '小甲鱼':
        list_boy.append(each_line[4:])
    elif each_line[:3] == '小客服':
        list_girl.append(each_line[4:])
    elif each_line[:3] == '===':
        num += 1
        pik_file = open('c:\\python\\boy_'+str(num)+'.txt','wb')
        pickle.dump(list_boy,pik_file)
        pik_file.close()
        pik_file = open('c:\\python\\girl_'+str(num)+'.txt','wb')
        pickle.dump(list_girl,pik_file)
        pik_file.close()
        list_boy = []
        list_girl = []
    
num += 1
pik_file = open('c:\\python\\boy_'+str(num)+'.txt','wb')
pickle.dump(list_boy,pik_file)
pik_file.close()
pik_file = open('c:\\python\\girl_'+str(num)+'.txt','wb')
pickle.dump(list_girl,pik_file)
pik_file.close()
list_boy = []
list_girl = []


for each in ['1','2','3']:
    pik_file = open('c:\\python\\boy_'+each+'.txt','rb')
    pik = pickle.load(pik_file)
    print('boy_%s.txt:' % each, pik)
    pik_file = open('c:\\python\\girl_'+each+'.txt','rb')
    pik = pickle.load(pik_file)
    print('girl_%s.txt:' % each, pik)

    
