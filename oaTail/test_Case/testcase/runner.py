# -*- coding: utf-8 -*-
from  oaTail.test_Case.models import testReport
if __name__ == '__main__':
        discover=testReport.addTc(rule='testLogin.py')
        testReport.beautifulReport(discover)

