list=[0,1,0,3,12,11]
list1=list
for i in range(0,len(list)):
    if list[i]==0:
        list1.pop(i)
        list1.insert(len(list),0)
print(list1)


