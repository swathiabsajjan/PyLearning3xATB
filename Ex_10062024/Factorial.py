# Program to find the factorial of a given number

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


num = int(input("Enter the number: "))
print("Factorial of a given number", num, "is", factorial(num))


