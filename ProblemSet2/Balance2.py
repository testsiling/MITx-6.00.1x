'''
MIT 6.00.1x Week 2 Problem set
Problem 2: Paying Debt off in a Year
Calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0

def bal(balance, month, fixPay):
    global monthlyInterestRate

    if month == 1:
        unpaid = balance - fixPay
        currentBal = unpaid + monthlyInterestRate * unpaid
        return currentBal

    #last month balance
    lastBal = bal(balance, month - 1, fixPay)
    #this month unpaid
    unpaid = lastBal - fixPay
    #totoal balance of this month
    currentBal = unpaid + monthlyInterestRate * unpaid
    
    return currentBal


balance = 3926
month = 12
guess = 10

while bal(balance, month, guess) >= 0:
    guess += 10

print("Lowest Payment: %d" %guess)








