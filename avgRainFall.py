# Write a program that uses nested loops to collect data and calculate the average rainfall over
# a period of years. The program should first ask for the number of years. The outer loop will
# iterate once for each year. The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of
# rainfall, and the average rainfall per month for the entire period.

numOfYears = int(input('Input the number of years: '))
months = 12
total = 0.0

for num in range(numOfYears):
    print('Year ', num + 1)
    print('------------------')
    for rain in range(months):
        print('Enter amount of rainfall in inches for month ', rain + 1, end = '')
        rainfall = float(input(' : '))
        total += rainfall
    totalMonths = numOfYears * months
    average = total / totalMonths
    print('\n===============================\n')

print('Total number of months are: ', totalMonths, )
print('Total inches of rainfall was', total, 'inches')
print('Average rainfall was ', average)
