# This program repeats string provided number of time
# Author: Rukhshan Alam

# defining a function
def repeat(s, number):
    result = ''
    # using loop to repeat string
    for r in range(0, number):
        result += s
    # returning the repeating result
    return result
# printing the function
print(repeat('Hi', 3))
