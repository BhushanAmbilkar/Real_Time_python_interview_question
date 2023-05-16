# Check leap Year

year = int(input("Enter a Year : "))

if ((year%400==0) or ((year%4==0) and (year%100!=0))):
    print("%d is leap year"%year)
else:
    print("%d is not a leap year"%year)


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
           return not leap
    else:
        return leap
print(is_leap(2016))