# check number is prime or not
num=11

for i in range(2,(num//2)+1):
    if num%i==0:
        print("%d is not a prime Number"%num)
        break
else:
    print("%d is prime number"%num)


#prime number from 1 to 100
for num in range(1,100):
    if num==0 or num==1:
        continue
    else:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
              break
        else:
              print("%d is prime number" % num)

def primenum(num):
    if num==0 or num==1:
        return "not a prime number"
    else:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
              break
        else:
              print("%d is prime number" % num)