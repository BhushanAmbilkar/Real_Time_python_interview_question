# Remove duplicate from list
l1 = [1, 2, 3, 1, 4, 5, 3, 3]

# Using In-Built function
print("List after removing duplicate element", list(set(l1)))

# Using for loop
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print("List after removing duplicate element", l2)

# Count of duplicate
dict1 = {}
for j in l2:
    if l1.count(j) > 1:
        dict1[j] = l1.count(j)
print("Duplicate element count", dict1)

# Duplicate elements
l3 = []
for i in l1:
    if l1.count(i) > 1 and l3.count(i) < 1:
        l3.append(i)

print("List of duplicate element", l3)

# Unique element
l4 = []
for i in l1:
    if l1.count(i) == 1:
        l4.append(i)
print("Unique elements :", l4)
