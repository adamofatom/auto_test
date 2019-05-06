# -*- coding: utf-8 -*-


import os
import xlrd
from oaTail.config.config import daPath
from oaTail.test_Case.models.log import Logger
import logging
log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class readExcel(object):
    def __init__(self,filename='elementDate.xlsx',sheetName='elementsInfo'):
        """

        :param filename:
        :param sheetName:
        """
        try:
            self.dataFile=os.path.join(daPath,filename)
            self.workbook=xlrd.open_workbook(self.dataFile)
            self.sheetName=self.workbook.sheet_by_name(sheetName)
        except Exception as e:
            log.logger.exception("init RadExcel fail")
            raise
        else:
            log.logger.info("initing  class readExcel")
    def readExcel(self,row,colnum):
        """

        :param row:
        :param colnum:
        :return:
        """

        try:

            value = self.sheetName.cell(row, colnum).value

        except Exception as e:
            log.logger.exception("read value from excel file fail")
            raise
        else:
            log.logger.info('reading value [%s] from excel file [%s] completed' % (value, self.dataFile))
            # raise
            return value
    def get_data(self):
        """
        适应ddt的方式
        :return: data
        """
        datatc=self.sheetName.row_values(0)
        rowsN=self.sheetName.nrows
        data=[]
        # dict={}
        for i in range(1,rowsN):
            tc1=self.sheetName.row_values(i)
            data.append(tc1)
        return data


if __name__ == '__main__':
    read=readExcel('oa.xlsx','login')
    a=read.readExcel(1,0)
    print(a)
    print(read.get_data())