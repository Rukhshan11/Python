# Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
# Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Corner Café —Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
# The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

message = ''

vegetarian = input('Is anyone at the party vegetarian? ')

if vegetarian == 'yes' or vegetarian == 'no':
    vegan = input('Is anyone at the party vegan? ')

    if vegan == 'yes' or vegan == 'no':
        glutenFree = input('Is anyone at the party gluten-free? ')
        if glutenFree == 'yes' or glutenFree == 'no':
            message = '\nHere is list of restaurants\n'

            if vegetarian == 'yes':

                if vegan == 'yes':

                    if glutenFree == 'yes' or glutenFree == 'no':
                        message += 'Corner Café\n' + \
                                   'The Chef’s Kitchen'
                else:
                    if glutenFree == 'yes':
                        message += 'Main Street Pizza Company\n' + \
                                   'Corner Café\n' + \
                                   'The Chef’s Kitchen\n'
                    else:
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"
            else:
                if vegan == "yes":

                    if glutenFree == "yes" or glutenFree == "no":
                        message += "Corner Cafe\nThe Chef's Kitchen\n"

                else:  # vegan == "no"

                    if glutenFree == "yes":
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"

                    else:  # gluten free == "no"
                        message += "Joe's Gourmet Burgers\n" + \
                                   "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"

        else:
            'Please answer with "yes" or "no". \nRe-run the program and try again'
    else:
        'Please answer with "yes" or "no". \nRe-run the program and try again'
else:
    'Please answer with "yes" or "no". \nRe-run the program and try again'
print(message)
