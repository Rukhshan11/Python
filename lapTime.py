#  asks the user to enter the number of times that they have run around a racetrack,
#  uses a loop to prompt them to enter the lap time for each of their laps.
# the program should display the time of their fastest lap, the time of
# their slowest lap, and their average lap time.

numOfLaps = int(input('Enter the number of times you ran around the race track. '))
slowestLap = 0.0
fastestLap = 0.0
total = 0.0

for laps in range(numOfLaps):
    print("LAP NO. ", laps + 1, end = '')
    lapTime = float(input(': '))

    total += laps

    if laps == 0:
        fastestLap = lapTime
        slowestLap = lapTime

    if slowestLap < lapTime:
        slowestLap = lapTime

    if fastestLap > lapTime:
        fastestLap = lapTime

    averageLapTime = total / numOfLaps

print('Slowest lap recorded is ', slowestLap)
print('Fastest lap recorded is ', fastestLap)
print('Average time of laps are ', averageLapTime)



