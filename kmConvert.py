# This program converts km to miles
# Author: Rukhshan Alam

def km():
    # 1 mile = 1 km * 0.
    # taking user input for distance to be converted to miles
    km = float(input('Enter the distance you want to convert to miles. '))

    # using formula to convert km into miles
    miles = km * 0.6214

    # printing the output
    print('The distance', km, ' km coverted into miles are ', miles, ' miles.')

# returning the function
km()
