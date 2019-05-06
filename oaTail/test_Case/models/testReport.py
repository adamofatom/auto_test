# -*- coding: utf-8 -*-
from oaTail.test_Case.models.log import Logger
import logging
import HTMLTestRunner
from BeautifulReport import BeautifulReport
from oaTail.config.config import rePath,tcPath
import os
import time
import unittest
log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)
def testreport():
    currtime=time.strftime('%Y-%m-%d %H_%M_%S')
    fileName=os.path.join(rePath,currtime+'.html')
    try:
        ftp=open(fileName,'wb')
    except Exception as e:
        log.logger.exception('[%s] open error cause Failed to generate test report' %fileName)
        raise e
    else:

        runner=HTMLTestRunner.HTMLTestRunner(stream=ftp,title="Oatail sys测试报告",description="'处理器:Intel(R) Core(TM) '\
                                                                    'i5-6200U CPU @ 2030GHz 2.40 GHz '\
                                                '内存:8G 系统类型: 64位 版本: windows 10 家庭中文版'")
        log.logger.info(' successed  to generate test report [%s]' % fileName)
        return runner
def beautifulReport(unit,description):
    """

    :param unit:
    :return:
    """
    currtime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = currtime+"_测试报告"
    try:
        result=BeautifulReport(unit)
        result.report(filename=fileName,description=description+"-测试报告",log_path=os.path.join(rePath,'report'))
    except Exception as e:
        log.logger.exception('[%s] open error cause Failed to generate test report' % fileName)
        raise e
    else:
        log.logger.info(' successed  to generate test report [%s]' % fileName)
def addTc(TCpath = tcPath, rule = 'test*.py'):
     """

    :param TCpath: 测试用例存放路径
    :param rule: 匹配的测试用例文件
     :return:  测试套件
    """
     discover = unittest.defaultTestLoader.discover(TCpath, rule)

     return discover
