# Task #1
# Explain the difference between the = operator and the == operator in Python.

# Assignment operator(=) :-

# It is used to assign the values to variables.
# It is used to assign values on the right side to left side of the variable.

#  For example,
a = 1
b = 2
c = a + b # assigns the value of a + b to c.
print(c)

# Comparison operator(==) :-

# It is used to compare Objects based on their values.
# It returns True if the values on both sides are equal, and False otherwise.
# It returns boolean values

# For example,
a = [1, 2, 3]
b = [1, 2, 3]
if (a == b):
    print("True")  # Returns True because a and b have same values
else:
    print("False")

a = [1, 2, 3]
b = [1, 2, 5]
if (a == b):
    print("True")
else:
    print("False")  # Returns False because a and b have different values


# What does the ** operator do in Python, and how is it used?
# ** operator is an Airthematic operator, it performs exponentiation,raising the first operand value to the right operand value.

#For example,
a = 2
b = 3
c = a ** b
print(c)

a = 10
b = -2
c = a ** b
print(c)

# What does the ^ operator do in Python, and in what context is it commonly used?
# Bitwise XOR(^) operator :-
# It is also known as exclusive OR operator. It is used to perform XOR operation between two operands.
# It returns true if and only if exactly one of the operand is true
# It compares each bit of its first operand to the corresponding bit of its second operand.
# If one bit is 0 and the other bit is 1, the corresponding result bit is set to 1 otherwise it is set to 0

# For example,
x = 7 # 0111 (8421)
y = 4 # 0100 (8421)
z = x ^ y # 0011
print(z)
