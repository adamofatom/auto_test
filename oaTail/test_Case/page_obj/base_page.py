# -*- coding: utf-8 -*-

import logging
from selenium import webdriver
from oaTail.test_Case.models import doExecl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from oaTail.test_Case.models import log
log=log.Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)
reEle=doExecl.readExcel('login.xlsx','elements')
reData=doExecl.readExcel('login.xlsx','data')
# driver=webdriver.Chrome
class basePage(object):
    menuList=\
        (

        )


    def __init__(self,driver,url):
        """

        :param driver:
        :param url:
        """
        self.driver=driver
        self.base_url=url
    def _open(self,url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.logger.exception(e,exc_info=True)
            raise ValueError('%s address access error, please check！' % url)
        else:
            log.logger.info('%s is accessing address %s at line[46]' % (sys._getframe().f_code.co_name, url))

    def open(self):
        """

        :return:
        """
        self._open(self.base_url)
        log.logger.info('%s loading successed!' % self.base_url)
        return self.base_url

    def findElement(self,*loc):
        """

        :param loc:
        :return:
        """
        try:
            element=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(loc)
            )
            print(loc)
        except Exception as e:

            log.logger.exception('finding element timeout!, details',exc_info=True)
            raise e
        else:
            log.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_element(*loc)

    def findElements(self,*loc):
        """

        :param loc:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(loc)
            )

        except Exception as e:

            log.logger.exception('finding element timeout!, details', exc_info=True)

            raise e
        else:
            log.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_elements(*loc)

    def jsScript(self,js):
        """

        :return:
        """
        try:
            self.driver.excute_script(js)
        except Exception as e:
            log.logger.exception('execute js script %s failed'%(js,))
            raise e
        else:
            log.logger.info('excute js script %ssuccessed '% (self, js))

    def inputValue(self,loc,value):
        """
        输入参数
        :param loc:
        :param value:
        :return:
        """
        element=self.findElement(*loc)
        try:
            element.clear()
            element.send_keys(value)
        except Exception as e:
            log.logger.exception('typing value error!', exc_info=True)

            raise e
        else:
            log.logger.info('inputValue:[%s] is receiveing value [%s]' % (loc, value))



    def getValue(self,*loc):
        """
        获取单个value值
        :param loc:
        :return:
        """
        element = self.findElement(*loc)
        try:
            value = element.text
        except Exception:
            value = element.get_attribute('value')
            log.logger.info('reading the element [%s] value [%s]' % (loc, value))
            return value
        except:
            log.logger.exception('read value failed', exc_info=True)
            raise Exception

        else:
            log.logger.info('reading the element [%s] value [%s]' % (loc, value))
            return value



    def getValues(self,*loc):
        """
        获取一组value
        :param loc:
        :return:
        """
        elements = self.findElements(*loc)
        value_list=[]
        try:
            for element in elements:
                value = element.text
                value_list.append(value)
        except:
            log.logger.exception('read value failed', exc_info=True)
            raise Exception

        else:
            log.logger.info('reading the element [%s] value [%s]' % (loc, value_list))
            return value_list
    def isElementExist(self,element):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
        except:
            return False
        else:
            return True