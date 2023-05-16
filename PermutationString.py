str1 = "ABC"

# Using itertools
from itertools import permutations

words = ["".join(i) for i in permutations(str1)]
print(words)

l = 0
a = list(str1)
n = len(str1)
if l == n:
    print("".join(a))
else:
    for i in range(l,n):
        a[l],a[i]=a[i],a[l]
        l+=1
        a[l],a[i]=a[i],a[l]

