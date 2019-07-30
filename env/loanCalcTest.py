#! usr/bin/env python3

def loanCalculator():

    term = 72
    month = 1
    interest_rate = .0545
    principal = 12000
    principal_payment = round(principal/term, 2)

    eachMonth = {}
    monthlyPayments = []

    while month <= term:

        interest = round(interest_rate * principal, 2)
        monthly_interest_payment = round(interest/12, 2)
        monthly_payment = round(monthly_interest_payment + principal_payment, 2)

        eachMonth['month'] = month
        eachMonth['monthly_payment'] = monthly_payment
        eachMonth['principal'] = principal

        monthlyPayments.append(eachMonth)
        thisMonth = monthlyPayments[month - 1]

        month = month + 1
        principal = round(principal - principal_payment, 2)

        print('Month:' + str(month), principal, interest, monthly_interest_payment, principal_payment, monthly_payment)
        print(thisMonth)














