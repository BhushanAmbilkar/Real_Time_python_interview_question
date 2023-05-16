str="Welcome to Python Programming"

s=str.count("m")
print(str.__sizeof__())
print(sorted(str))

str2="abababa"
s=[]
for i in range(len(str2)):
    for j in range(i+1,len(str2)+1):
        temp=str2[i:j]
    s.append(temp)
print("mm",s)
temp1=" ".join(s[::-1])
res={}
print(temp1)
for i in temp1:
    if i not in res.keys():
        res[i]=1
    else:
        res[i]+=1
print(res)

# Python3 code to demonstrate working of
# All substrings Frequency in String
# Using list comprehension

# initializing string
test_str = "abababa"

# printing original string
print("The original string is : " ,test_str)

# list comprehension to extract substrings and frequency
res = dict()
for ele in [test_str[idx: j] for idx in range(len(test_str)) for j in range(idx + 1, len(test_str) + 1)]:
    res[ele] = 1 if ele not in res.keys() else res[ele] + 1

# printing result
print("Extracted frequency dictionary : ", res)



