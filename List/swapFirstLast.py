list1 = [12, 35, 9, 56, 24]
Output = [24, 35, 9, 56, 12]
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp

print(list1)

def swaplist(list1):
    list1[0], list1[-1] =list1[-1], list1[0]
    return list1
list1=[12, 35, 9, 56, 24]
print(swaplist(list1))