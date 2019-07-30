# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from loanCalculator import *
#---------------------------------------------------------------
def runTests():

    test_constructor()
    test_constructorWithBadData()
    test_calculator_2()
    test_calculator()

#-----------------------------------------------------------------------------
def test_constructor():

    print("--- test_constructor")

    loan_calculator = LoanCalculator(product_name = "Some car or other",
                                     interest_rate = .0345,
                                     principal = 40000,
                                     month = 49,
                                     term = 72)
    assert(loan_calculator.validObject())

#------------------------------------------------------------------------------
def test_constructorWithBadData():

     print("--- test_constructorWithBadData")

     loan_calculator = LoanCalculator(product_name = "Another car",
                                      interest_rate = .0235,
                                      principal = -30000,
                                      month = 36,
                                      term = 48)
     assert(not loan_calculator.validObject())

#-------------------------------------------------------------------------------
def test_calculator_2():

    print("--- print_results")
    loan_calculation_2 = LoanCalculator('Bolt EV', 0.0545, 25000, 0, 72)
    results = loan_calculation_2.loanCalculator()
    print(results)

#------------------------------------------------------------------------------
def test_calculator():

    print("--- test_calculation")
    loan_calculation = LoanCalculator('Bolt EV', 0.0545, 25000, 0, 72)
    month = loan_calculation.loanCalculator()
    monthly_payment = loan_calculation.loanCalculator()
    principal = loan_calculation.loanCalculator()
    term = loan_calculation.loanCalculator()
    assert(month == 1 and monthly_payment == 460.76 and principal == 24652.78 and term == 72)

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    runTests()

