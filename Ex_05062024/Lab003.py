print()
# self, *args, sep='', end='\n', file=None
# self - Concepts in Oops which points to itself - ignore
# *args - Unlimited number of argumenrs * - strings, int, float, boolean...
# sep='' - How you want to seperate the arguments
# end='\n' - In the end what you want to do. By default \n(new-line) is the value.
# file=None - File IO

print("Hello", "World", 123, True, 3.14)
print("Hello", "World", 123, True, 3.14, sep='-')
# Only one seperator in one print command, we can't use multiple seperator in single print command
print("Hello", "World", 123, True, 3.14, sep='#')
print("Hi, My name is Swathi", "Sajjan", sep=' - ')

print("Hi", "Swathi", "Sajjan", sep="-", end="\t")
print("Hi", "Swathi", "Sajjan")

# print(sep="-", "Hi", "Swathi") SyntaxError: positional argument follows keyword argument
# First we have to pass the arguments followed by seperator & end.

print("I am", "a Good Person", sep=" ", end="_")
print("I am a Bad Person")

#Python is case-sensitive
#Print("Hi")
