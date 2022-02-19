# Write a program that calculates the amount of money a person would earn over a period of
# time if his or her salary is one penny the first day, two pennies the second day, and continues
# to double each day. The program should ask the user for the number of days. Display
# a table showing what the salary was for each day, then show the total pay at the end of the
# period. The output should be displayed in a dollar amount, not the number of pennies.

days = int(input('Input the number of days you worked. '))
totalSalary = 0.0
print('Days\tSalary')
print('-' * 30)

for nums in range(1, days + 1):
    salary = 0.01 * 2 ** (nums - 1)
    totalSalary += salary
    print(nums, '\t', salary)
print('\nTotal pay at the end of pay period is $', totalSalary)
