# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 == side 3

side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

if side1 == side2 and side2 == side3 and side3 == side1:
    print("Triangle is Equilateral Traignle.")
elif side1 == side2 or side2 == side3:
    print("Triangle is Isosceles Triangle.")
else:
    print("Trianlge is not Equlateral or Isosceles ")

