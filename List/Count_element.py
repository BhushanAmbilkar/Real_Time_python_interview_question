lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

# count single element
print(lst.count(10))

# count single element Using for loop
count=0
for i in lst:
    if i=="10:":
        count+=1
print("10",count)

# Using pandas
# import pandas as pd
# count=pd.Series(lst).value_counts()
# print(count)

# Using Counter
from collections import Counter
d=Counter(lst)
print(d)

# 10 occurrence Using Counter()
print('{} has occurred {} times'.format(10,d[10]))