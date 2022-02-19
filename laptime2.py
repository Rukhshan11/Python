Lap_count=int(input('How many laps you have taken '))
slowest_lap=0.0
Fastest_lap=0.0
total=0.0
for num in range(Lap_count) :
         print('This is the input for lap ', num+1,)
         lap_time = float(input('Enter the lap time: '))
         print('=======================================')
         if num == 0 :
             slowest_lap = lap_time
             Fastest_lap = lap_time
         total += lap_time
         if  slowest_lap < lap_time:
             slowest_lap = lap_time
         if Fastest_lap > lap_time:
             Fastest_lap = lap_time

print('The fastest lap is:', Fastest_lap)
print('The slowest lap is:', slowest_lap)
print('The averages is:', format((total/Lap_count), '.2f'))