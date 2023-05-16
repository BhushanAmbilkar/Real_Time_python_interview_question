list1 = [1, 2, 3, 4, 5, 6, 7]
# Using the slicing
print(list1[::-1])

# Using for loop and insert
l1 = []
for i in list1:
    l1.insert(0,i)
print(l1)

# Using the reversed and reverse built-in function
list2=list1
list2.reverse()
print("Using reverse():-",list2)
print("Using reversed()", list(reversed(list2)))
