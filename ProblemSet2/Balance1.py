'''
MIT 6.00.1x Week 2 Problem set
Problem 1: Paying Debt off in a Year

calculate the credit card balance after one year
if a person only pays the minimum monthly payment
required by the credit card company each month.
'''

balance = 42
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentRate = 0.04
month = 12


def bal(balance, month):
    global monthlyInterestRate
    global monthlyPaymentRate

    if month == 1:
        unpaid = balance - balance * monthlyPaymentRate
        currentBal = currentBal = unpaid + monthlyInterestRate * unpaid
        print("Month %d Remaining balance: %.2f" % (month, currentBal))
        return currentBal

    #last month balance
    lastBal = bal(balance, month - 1)

    #this month unpaid
    unpaid = lastBal - lastBal * monthlyPaymentRate

    #totoal balance of this month
    currentBal = unpaid + monthlyInterestRate * unpaid
    print("Month %d Remaining balance: %.2f" % (month, currentBal))
    return currentBal


print("Remaining balance: %.2f" % (bal(balance, month)))




