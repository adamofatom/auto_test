# -*- coding: utf-8 -*-
from selenium import webdriver
import logging
import sys
from oaTail.test_Case.models.log import Logger
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class wDriver(object):
    def chromeDriver(self):
        """
        chrome driver
        :return:
        """
        try:
            self.driver=webdriver.Chrome()
        except Exception as e:
            log.logger.exception('ChromeDriverServer.exe executable needs to be in PATH. Please download!',exc_info=True)
            raise e
        else:
             log.logger.info('%s:found the chrome driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
             return self.driver
    def ieDriver(self):
        """
        chrome driver
        :return:
        """
        try:
            self.driver=webdriver.Ie()
        except Exception as e:
            log.logger.exception('ieDriverServer.exe.exe executable needs to be in PATH. Please download!',exc_info=True)
            raise e
        else:
             log.logger.info('%s:found the ie driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
             return self.driver
    def fireDriver(self):
        """
        chrome driver
        :return:
        """
        try:
            self.driver=webdriver.Firefox()
        except Exception as e:
            log.logger.exception('FireDriverServer.exe executable needs to be in PATH. Please download!',exc_info=True)
            raise e
        else:
             log.logger.info('%s:found the fire driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
             return self.driver
if __name__ == '__main__':
    wdriver=wDriver()
    wdriver.chromeDriver()