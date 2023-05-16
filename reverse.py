#type 1

str ="mahesh wagge"
#---1
rev_str=str[::-1]

#---2
rev_str1="".join(reversed(str))

#----3
rev=""
for i in str:
    rev=i+rev

print("Type 1",rev)
print("Type 2",rev_str)
print("Type 3",rev_str1)

#---- 4
list1=str.split()
str2=" ".join(list1[::-1])
print(str2)

#-- 5
rev_str3=[]
for i in list1:
    rev_str3=[i] + rev_str3
print(rev_str3)
print(" ".join(rev_str3))

#--- 6
list2=[]
for i in list1:
    list2.append(i[::-1])
print(" ".join(list2))



