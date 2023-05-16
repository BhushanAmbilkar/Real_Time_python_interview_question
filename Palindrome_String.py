str1 = input("Enter a string: ")

# method 1
str2 = ' '
index = -1
for i in str1:
    str2 += str1[index]
    index -= 1

print("The given string = {} \nThe Reversed string = {}".format(str1, str2))

if str1 == str2:
    print("Hence, the given string is Palindrome")
else:
    print("Hence, the given is not a palindrome")

# method 2
str3=""
for i in str1:
    str3 = i + str3
if str1 == str3:
    print("Hence, the given string is Palindrome")
else:
   print("Hence, the given is not a palindrome")



