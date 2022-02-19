# 10 hot dogs in 1 package
# 8 buns in 1 package
# calculate number of packages of hot dogs and buns
# calculate leftover
# min packages required

hotDogsPerPack = 10
bunsPerPack = 8

peopleAttending = int(input('Enter number of people attending cookout: '))
hotDogsPerPerson = int(input('Enter number of hotdogs per person: '))
totalNumberOfHotdogs = peopleAttending * hotDogsPerPerson

reqHotDogsPack = totalNumberOfHotdogs // hotDogsPerPack
reqBunsPack = totalNumberOfHotdogs // bunsPerPack
hotDogsLeftover = totalNumberOfHotdogs % hotDogsPerPack
bunsLeftOver = totalNumberOfHotdogs % bunsPerPack

print('Hot dogs packages required: ', reqHotDogsPack)
print('Buns packages required ', reqBunsPack)
print('hot dogs leftover', hotDogsLeftover)
print('Buns left over', bunsLeftOver)