# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
# application that displays the number of millimeters that the ocean will have risen each year
# for the next 25 years


yearRise = 1.6
calRise = 0.0

print('Year \tRise in Ocean Level(im mm) ')
for r in range(1, 26, 1):
    calRise = r * yearRise
    print(r, '\t ', calRise,'mm')