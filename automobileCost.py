# Write a program that asks the user to enter the monthly costs for the following expenses
# incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
# maintenance. The program should then display the total monthly cost of these expenses,
# and the total annual cost of these expenses.

# Rukhshan Alam

def expenses():
    # Getting the cost of expenses from user "loanPayment, insurance, gas, oil, tires, maintainance."
    loanPayment = float(input('Enter monthly payment: $'))
    insurance = float(input('Enter monthly insurance: $'))
    gas = float(input('Enter monthly gas expanse: $'))
    oil = float(input('Enter monthly oil change expense: $'))
    tires = float(input('Enter monthly expense on tires: $'))
    maintenance = float(input('Enter monthly cost on other maintenances: $'))
    monthlyCost(loanPayment, insurance, gas, oil, tires, maintenance)

def monthlyCost(loanPayment, insurance, gas, oil, tires, maintenance):
    # Calculating and printing average monthly expenses of automobile
    totalMonthlyCost = loanPayment + insurance + gas + oil + tires + maintenance
    print('\nAverage monthly expense of automobile is $', format(totalMonthlyCost, '.2f'), sep='')
    yearlyCost(totalMonthlyCost)

def yearlyCost(totalMonthlyCost):
    # Calculating and printing average yearly expenses of automobile
    yearlyExpense = totalMonthlyCost * 12
    print('Average yearly expense of automobile is $', format(yearlyExpense, '.2f'), sep='')
expenses()

