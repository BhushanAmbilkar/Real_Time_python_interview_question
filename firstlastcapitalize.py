# Python program to capitalize
# first and last character of
# each word of a String

s = "welcome to python"
print("String before:", s)
a = s.split()
res = []
for i in a:
    x = i[0].upper() + i[1:-1] + i[-1].upper()
    res.append(x)
res = " ".join(res)
print("String after:", res)
