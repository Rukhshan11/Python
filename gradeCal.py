#Grade Calculator
# test = 25
# exam = 50
message = ""
test1 = float(input('Please input the marks obtained in test 1: '))

if test1 >= 0 and test1 <= 25:
    test2 = float(input('Please input the marks obtained in test 2: '))

    if test2 >= 0 and test2 <= 25:
        exam = float(input('Please enter the marks obtained in Exam: '))

        if exam >= 0 and exam <= 50:
            total_marks = test1 + test2 + exam

            if total_marks > 50 and exam > 25:
                if total_marks > 80:
                    message = "Distinction"
                elif total_marks <= 80 and total_marks >= 60:
                    message = "Credit"
                elif total_marks < 60:
                    message = 'Pass'
            else:
                message = "Fail, Marks too low"
        else:
                message ='Exam marks should be between 0-50. ' + \
                    'Re-run the program'
    else:
            message = 'Test 2 marks should be between 0 - 25 ' + \
                        'Re-run the program'
else:
        message = 'Test 1 marks should be between 0 - 25 ' + \
                  'Re-run the program'

print(message)



