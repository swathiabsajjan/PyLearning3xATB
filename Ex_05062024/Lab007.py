# Some rules to create a variable name
# Variable name should be start from A-Z, a-z
name = "Swathi"
print(type(name))

#Variable name should not start with number
#123 = 345 -> variable name should not start with any number

#Variable name should not be any keyword
# Keyword // Reserved word
# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield' [2]
#Their are 35 keywords in Python
# Example :- and = 123

#Variable name should not be any special character
# @ = 123
# $ = -123
_ = 123 #Variable name have the option to start with '_' special character.
_name = "Swathi_Karthik"
# @pramod = "pramod"
# pramod@ = "pramod" # Variable name should not start with variable name followed by special character

# Variable name should not be any space
# fisrt name = "Pramod"
first_name = "Pramod"

#Python love the snake case
variable_name = "Pramod" # Instaed of spaace wee can use '_' as the space between fisrt character and second character.

long_variable_name_is_created_here = "hello" # Variable name length has no limit.