# -*- coding: utf-8 -*-
from oaTail.test_Case.models.myunittest import MyTestCase
import unittest
import os
from oaTail.test_Case.models import testReport
from oaTail.test_Case.page_obj.loginPage import loginPage
from oaTail.config.config import imPassPath
import logging
from oaTail.test_Case.models import log
log=log.Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)
class loginTest(MyTestCase):
    def testImage(self):
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(os.path.join(imPassPath,'login.png'))
        self.driver.implicitly_wait(3)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(loginTest('testImage'))
    testReport.beautifulReport(suite)