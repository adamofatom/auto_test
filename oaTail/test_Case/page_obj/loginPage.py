# -*- coding: utf-8 -*-
from oaTail.test_Case.page_obj.base_page import basePage,reData,reEle
from selenium.webdriver.common.by import By
from oaTail.test_Case.models import log
import logging
import sys
log = log.Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class loginPage(basePage):
        userNameEle = (By.XPATH, reEle.readExcel(1, 0))

        passWordEle = (By.XPATH, reEle.readExcel(1, 1))

        loginBtnEle = (By.XPATH, reEle.readExcel(1, 2))

        def clickLoginBtn(self):
            element=self.findElement(*self.loginBtnEle)
            element.click()

        def loginFunc(self, username=reData.readExcel(1,0), password=reData.readExcel(1,1)):
                """
                :param username:
                :param password:
                :return:
                """
                self.inputValue(self.userNameEle, username)

                self.inputValue(self.passWordEle, password)

                self.clickLoginBtn()

