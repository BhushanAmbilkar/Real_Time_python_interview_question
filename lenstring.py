# Python code to demonstrate string length
# using len
str1 = "mahesh wagge"
print(len(str1))


# using for loop

# Returns length of string
def findlen(str2):
    counter = 0
    for i in str2:
        counter += 1
    return counter

str2 = "Mahesh Wagge"
print(findlen(str))
