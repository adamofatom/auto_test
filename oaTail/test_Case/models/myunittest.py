# -*- coding: utf-8 -*-
import unittest
from oaTail.test_Case.models.log import Logger
import logging
from oaTail.test_Case.models.driver import wDriver
# from selenium.webdriver.common.by import By
from oaTail.test_Case.page_obj.loginPage import loginPage
import time
log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        wd=wDriver()
        cls.driver=wd.chromeDriver()
        cls.driver.maximize_window()
        log.logger.info("open the browser success")
    def setUp(self):
         # self.driver.find_element
        self.login=loginPage(self.driver,'http://127.0.0.1:8069/login')
        self.login.open()
        self.login.loginFunc()
        log.logger.info('************************starting run test cases************************')
    def tearDown(self):
        self.driver.refresh()
        log.logger.info('************************test case run complete************************')
        # print(222)
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
        log.logger.info("quit the browser success")

if __name__ == '__main__':
    unittest.main()
