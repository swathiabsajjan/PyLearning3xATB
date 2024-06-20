# create a program that determines whether a given number is a leap year.
# A Leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determinaion

year = int(input("Enter the year: "))
if year%4 == 0 and year%400 == 0:
     print("Leap Year")
elif year%100 != 0:
    print("Not a Leap Year")