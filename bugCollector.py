# A bug collector collects bugs every day for five days. Write a program that keeps a running
# total of the number of bugs collected during the five days. The loop should ask for the
# number of bugs collected for each day, and when the loop is finished, the program should
# display the total number of bugs collected.

days = 5
totalBugsCollected = 0.0
for bugs in range(days):
    print('Bugs collected on day', bugs + 1, end='')
    bugsCollectedEachDay = int(input(': '))
    # Add the score to the accumulator.
    totalBugsCollected += bugsCollectedEachDay
print('Total bugs collected by collector are', + totalBugsCollected)
