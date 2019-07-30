# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from loanCalcTest import *

#---------------------------------------------------------------
def runTest():

    carLoan = loanCalculator()
    print(carLoan)

#---------------------------------------------------------------
if __name__ == '__main__':
    runTest()