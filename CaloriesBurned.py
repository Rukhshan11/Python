#
#
#
#

caloriesBurnedPerMin = 4.2

for minutes in range (10, 31, 5):
    calories = caloriesBurnedPerMin * minutes
    print("You will burn ", calories, " calories in ", minutes, " minutes.")

