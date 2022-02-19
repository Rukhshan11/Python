# Write a program that displays a table of distances in miles and their equivalent distances in
# kilometers, rounded to 2 decimal places. One mile is equivalent to 1.60934 kilometers. The
# table should be generated using a loop, and should include values in 10 mile increments from
# 10 to 80

mileToKm = 1.60934
print('MILES\tKM')
print('===========')

for mile in range(10, 81, 10):
    km = mileToKm * mile
    print(mile, '\t', km )
