list1=["mahesh","mahi","mahraj","juio"]
str="mahesh"
j=""
list2=[]
for i in str[-5:-2:1]:
    j=j+i
  #  print(j)
    for n in list1:
        if j in n:
            list2.append(n)

print(set(list2))

p=[]
for l in list2:
    if l not in p:
        p.append(l)
print(p)