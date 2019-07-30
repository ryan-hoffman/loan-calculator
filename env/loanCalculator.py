#! usr/bin/env python3

# loanCalculator.py: a class that calculates the...
#
# monthly principal payment
# monthly interest payment
# total monthly payment
# monthly decrease in principal
# tracks month
#
# ...returns these values and also returns a dict containing
# {month:new_month, monthly_payment:new_monthly_payment, principal:new_principal}
#
# However, it doesn't do all that yet!
#
# ToDo: correct interest calculation to be re-calculated yearly (or daily)


class LoanCalculator():

    product_name = None
    interest_rate = None
    principal = None
    month = None
    term = None

    def __init__(self, product_name, interest_rate, principal, month, term):

        self.product_name = product_name
        self.interest_rate = round(interest_rate, 4)
        self.principal = round(principal, 2)
        self.month = month
        self.term = term

    def validObject(self):

        validProductName = len(self.product_name) > 0
        validInterestRate = isinstance(self.interest_rate, (int, float)) and self.interest_rate > 0
        validPrincipal = isinstance(self.principal, (int, float)) and self.principal > 0
        validMonth = isinstance(self.month, (int, float)) and self.month > 0
        allTests = [validProductName, validInterestRate, validPrincipal, validMonth]
        return(all(allTests))

        # all() returns True when all items in the given iterable are true

    def show(self):

        print("--- a LoanCalculator Object for a loan with these values ---")
        print("Product Name: %s" % self.product_name)
        print("Interest Rate: %f" % self.interest_rate)
        print("Principal: $%f" % self.principal)
        print("Month: %f" % (self.month))
        print("Term: %f" % (self.term) + " months.")

    def loanCalculator(self):

        eachMonth = {}
        monthlyPayments = []

        principal_payment = round(self.principal/self.term, 2)

        while self.month <= self.term:

            interest = round(self.interest_rate * self.principal, 2)
            monthly_interest_payment = round(interest/12, 2)
            monthly_payment = round(monthly_interest_payment + principal_payment, 2)

            eachMonth['month'] = self.month
            eachMonth['monthly_payment'] = monthly_payment
            eachMonth['principal'] = self.principal - principal_payment

            monthlyPayments.append(eachMonth)
            thisMonth = monthlyPayments[(self.month - 1)]

            month = self.month + 1
            principal = round(self.principal - principal_payment, 2)

            return(month, principal, interest, monthly_interest_payment, principal_payment, monthly_payment, thisMonth)





