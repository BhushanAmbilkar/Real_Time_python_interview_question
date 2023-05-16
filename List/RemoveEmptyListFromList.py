l1 = [5, 6, [], 3, [], [], 9]
l2=[]
for i in l1:
    if i!=[]:
        l2.append(i)
print(l2)

print(l1[:])
l3=[]
l3.extend(l1)
print(l3)