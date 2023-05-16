list = [1, 2, 3]
l=[[]]
for i in range(len(list)+1):
    for j in range(i):
        l.append(list[j:i])
print(l)