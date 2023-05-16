def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n * facto(n-1)
n = int(input("Enter a Number : "))
print(facto(n))



def fact1(n):
    if n<0:
        return "invalid input"
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while n>1:
            fact*=n
            n-=1
        return fact
n=5
print(fact1(n))