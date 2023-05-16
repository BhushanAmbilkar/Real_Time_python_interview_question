# Count character
str1 = " I am Python Developer "
str2 = "".join(set(str1))
print(str2)
count = {}.fromkeys(str2, 0)
for i in str1:
    count[i] += 1
print(count)

n = 0
for i in str1:
    if "e" == i:
        n += 1
print(n)

print(str1.count("e"))

chardict = {}
for num in str1:
    keys = chardict.keys()
    if num in keys:
        chardict[num] += 1
    else:
        chardict[num] = 1

print(chardict)

