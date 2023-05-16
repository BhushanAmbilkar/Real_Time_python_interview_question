l1 = [20, 10, 20, 1, 100]

# Using Built_In function
# print(min(l1))

# Using loop
min1 = l1[0]
for i in range(len(l1)):
    if l1[i] < min1:
        min1 = l1[i]
print(min1)

# Using sort function (ascending order)
l1.sort()
print(l1[0])

# Using sort function (Descending order)
l1.sort(reverse=True)
print(l1[-1])
