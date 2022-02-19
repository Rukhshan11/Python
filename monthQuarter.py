

userInput = int(input('Please enter a month to determine its quarter '))
message = ""

if userInput < 1 or userInput > 12:
    print('Error, Please enter a valid month ')
else:
    message += " \nMonth " + format(userInput) + " is in the"

    if userInput >= 1 and userInput <= 3:
        message += ' First'
    elif userInput >= 4 and userInput <= 6:
        message += ' Second'

    elif userInput >= 7 and userInput <= 9:
        message += ' Third'

    elif userInput >= 10 and userInput <= 12:
        message += 'Fourth'
    message += ' qaurter. \n'
print(message)

