# Function for nth fibonacci

def fibonacci(n):
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            return b


# Driver Program
print(fibonacci(2))

# def Fib(n):
#     if n<0:
#         print("Incorrect input")
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return Fib(n-1) + Fib(n-2)
# n=8
#
# for i in range(n):
#     print(Fib(i))
