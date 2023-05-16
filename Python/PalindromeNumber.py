number = int(input("Enter a Number : "))
reverse = 0
temp = number

while (temp > 0):
    Reminder = temp % 10
    reverse = (reverse * 10) + Reminder
    temp = temp // 10

print("Reverse of it is = %d" % reverse)

if (number == reverse):
    print("%d is a Palindrome" % number)
else:
    print("%d is Not Palindrome" % number)