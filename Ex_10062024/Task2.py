# Develop a Python script that calculates the square and cube of a given number.

n = 2
square = n ** 2
cube = n ** 3
print(f"Square of {n} is {square}")
print(f"Cube of {n} is {cube}")

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = input("Enter First number: ")
num2 = input("Enter Second number: ")
num1 = int(num1)
num2 = int(num2)
print(f"{num1} is {'greater than' if num1 > num2 else 'less than' if num1 < num2 else 'equal to'} {num2}.")

