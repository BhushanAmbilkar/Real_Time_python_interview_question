# Python code find whether a list
# exists in list of list.
import collections

# Input List Initialization
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]

# List to be searched
list_search = [2, 3, 4]

# Flag initialization
flag = 0

# Using Counter
for elem in Input:
    if collections.Counter(elem) == collections.Counter(list_search):
        flag = 1

# Check whether list exists or not.
if flag == 0:
    print("False")
else:
    print("True")
for elem in Input:
    if elem == list_search:
        print(elem)
