list1=[1,4,2,10,7]
#list1 = ["mahesh", "arun", "vijay"]
#list1.sort()
# print(list1)

a = []
for i in range(len(list1)):
    a.append(min(list1))
    list1.remove(min(list1))
print(a)

strings = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']

for i in range(len(strings)):
    for j in range(i + 1, len(strings)):
        if strings[i] > strings[j]:
            strings[i], strings[j] = strings[j], strings[i]

print(strings)

def sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(0, len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    print(list1)
#l=[1,3,2,10,4]
l= [1, 4, 2, 10, 7]
sort(l)