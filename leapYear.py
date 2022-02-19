#
#
#

userInput = int(input('Please enter the year: '))
message = ""

if userInput <= 0:
    message = 'Please enter a valid year ' + \
               'Re-run the program and try again'

else:
    message = 'In ' + format(userInput) + ', February has'
    if userInput % 100 == 0:
        if userInput % 400 == 0:
            message += ' 29 days'
        else:
            message += ' 28 days'
    else:
        if userInput % 4 == 0:
            message += ' 29 days'
        else:
            message += ' 28 days'
print(message)
