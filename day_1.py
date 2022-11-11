# Exercise 2: Fix the code below

# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Exercise 3: Write a program that prints the number of characters in a user's name.
# You might need to Google for a function that calculates the length of a string.

name = input('What is your name?')
print(len(name))

# Write a program that switches the values stored in the variables a and b.

a = int(input('Variable "a" is:'))
b = int(input('Variable "b" is:'))

a, b = b, a
print(f'a = {a}')
print(f'b = {b}')

c = a
a = b
b = c
print(f'a = {a}')
print(f'b = {b}')
