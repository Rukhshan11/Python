#
#
#
message = ""
userDAY = int(input('Please Enter two digit day '))
userMonth = int(input('Please Enter two digit month '))
userYear = int(input('Please Enter two digit year '))

message += format(userDAY) + '/' + \
            format(userMonth) + '/' + \
            format(userYear) + \
            ' IS'
if ((userDAY * userMonth) != userYear):
    message += ' NOT'

message += ' Magic'

print(message)