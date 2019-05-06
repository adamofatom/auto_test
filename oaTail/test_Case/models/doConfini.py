# -*- coding: utf-8 -*-
import logging
import configparser
from oaTail.test_Case.models.log import Logger
log=Logger(__name__,logging.INFO,logging.INFO)
class doConfini(object):
    def __init__(self):
        self.cf=configparser.ConfigParser()

    def getConfValue(self,filename,section,name):
        try:
            self.cf.read(filename)
            value=self.cf.get(section,name)
        except Exception as e:
            log.logger.exception("read file[%s] for [%s] failed ,don't get the value"%(filename,section))
            raise e
        else:
            log.logger.info("read excel value [%s] successed"%value)
            return value
    def writeConfValue(self,filename,section,name,value):
        """

        :param filename:
        :param section:
        :param name:
        :param value:
        :return:
        """
        try:
            self.cf.add_section(section)
            self.cf.set(section,name,value)
            self.cf.write(open(filename,'w'))
        except Exception as e:
            log.logger.exception('section %s has been exist!' % section)
            # log.logger.exception("write file[%s] failed ,don't write the value"%(filename,))
            raise configparser.DuplicateSectionError(section)
        else:
            # log.logger.info("write excel value [%s] successed"%value)
            log.logger.info('write section' + section + 'with value ' + value + ' successed!')