# Check Number is Armstrong or not
input_num = int(input(f" Enter a Number : " ))
num = input_num
a = len(str(num))
arm = 0
print(a)
while num > 0:
    r = num % 10
    arm = arm + r ** a
    num = num // 10
if input_num == arm:
    print("the number is an Armstrong number")
else:
    print("the number is not an Armstrong number")

# method 2
num_arm = 153
length_num = len(str(num_arm))
a = list(map(int, str(num_arm)))
b = list(map(lambda x: x ** length_num, a))
if sum(b) == input_num:
    print("the number is an Armstrong number")
else:
    print("the number is not an Armstrong number")
