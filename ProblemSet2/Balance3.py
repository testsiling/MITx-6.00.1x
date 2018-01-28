'''
MIT 6.00.1x Week 2 Problem set
Problem 3 - Using Bisection Search to Make the Program Faster
Calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.
Using Bisection Search.

Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

def bal(balance, month, fixPay):
    global monthlyInterestRate

    if month == 1:
        unpaid = balance - fixPay
        currentBal = unpaid + monthlyInterestRate * unpaid
        return currentBal

    # last month balance
    lastBal = bal(balance, month - 1, fixPay)
    # this month unpaid
    unpaid = lastBal - fixPay
    # total balance of this month
    currentBal = unpaid + monthlyInterestRate * unpaid

    return currentBal

annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0
balance = 999999
month = 12

lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

guess = (lowerBound + upperBound) / 2.0
remain = bal(balance, month, guess)

while round(remain, 2) != 0:

    # print(round(remain, 2))
    # if monthly pay not enough
    if remain > 0:
        lowerBound = guess

    # if pay too much
    if remain < 0:
        upperBound = guess

    guess = (lowerBound + upperBound) / 2.0
    remain = bal(balance, month, guess)

print("Lowest Payment: %.2f" % guess)








