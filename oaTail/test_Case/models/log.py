# -*- coding: utf-8 -*-
import logging
import time
# from  oaTail.config.config import logPath
class Logger(object):
    def __init__(self, logger, CmdLevel=logging.INFO, FileLevel=logging.INFO):
       """

       :param logger:
       :param CmdLevel:
       :param FileLevel:
       """
       self.logger = logging.getLogger(logger)
       self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
       # 日志输出格式
       fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
       # 日志文件名称
       currTime = time.strftime("%Y-%m-%d")
       self.LogFileName = r'/home/gu/PycharmProjects/auto_test/oaTail/report/log/' + currTime + '.log'
       # self.LogFileName=logPath+currTime+'.log'
       # 设置文件输出
       fh = logging.FileHandler(self.LogFileName)
       fh.setFormatter(fmt)
       fh.setLevel(FileLevel)  # 日志级别
       self.logger.addHandler(fh)
