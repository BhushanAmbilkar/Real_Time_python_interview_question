# Efficient program to print all prime factors of a given number

def PrimeFactor(n):

    for i in range(2,n+1):
        if n%i==0:
            for j in range(2, (i // 2) + 1):
                if i % j == 0:

                    break
            else:
                print(i)
n=1092
print(PrimeFactor(n))