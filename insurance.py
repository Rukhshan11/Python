# Many financial experts advise that property owners should insure their homes or buildings
# for at least 80 percent of the amount it would cost to replace the structure. Write a program
# that asks the user to enter the replacement cost of a building, then displays the minimum
# amount of insurance he or she should buy for the property

# Author: Rukhshan Alam


def buildingCost():

    # Asking user fo replacement cost of the building
    rebuildCost = float(input('How much amount of money will take to rebuild this building? $'))

    def insurance():
        # calculating the insurance needed for user provided building cost
        insuranceNeed = rebuildCost * .80

        # Printing the output of insurance calculation
        print('Minimum insurance needed on this building is $', format(insuranceNeed, '.2f'), sep='')
    insurance()
buildingCost()