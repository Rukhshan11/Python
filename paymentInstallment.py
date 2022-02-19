# Payment Installment

totalPurchase = float(input('The total of your purchase is $'))
desiredInstallment = int(input('How many installments would to like to put this into? '))

interestTotal = totalPurchase * 0.05
Total = interestTotal + totalPurchase

installmentPayment = Total / desiredInstallment

print('Your subtotal is', totalPurchase, 'after installment plan your total will be', Total, ' dollars, and you will pay that in',
      desiredInstallment, ' installments, your each installment will be', installmentPayment, 'dollars')
