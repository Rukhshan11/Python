# 13. Population
# Write a program that predicts the approximate size of a population of organisms. The
# application should use text boxes to allow the user to enter the starting number of organisms, the average
# daily population increase (as a percentage), and the number of days the
# organisms will be left to multiply.

startingNum = int(input('Starting number of organism '))
increaseRate = float(input('Enter Average daily increase [%]. ')) / 100
days = int(input('Enter days '))
print('\nDay\t |Estimated Population')
print('=' * 20)
initial = True

for days in range(1, days + 1):
    if initial:
        print(1, '\t |', startingNum)
        initial = False

    startingNum *= (1 + increaseRate)
    print(days , '\t |', startingNum)



