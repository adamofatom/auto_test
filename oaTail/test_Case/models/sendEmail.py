# -*- coding: utf-8 -*-
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from oaTail.config.config import rePath,daPath
from oaTail.test_Case.models.log import Logger
import os
log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)
class sendEmail(object):
    def __init__(self,subject,server='smtp.qq.com',fromUser="905949017@qq.com",sqm='aaaaaa',toUser="guch@bankcall.net"):
        self._server=server
        self._subject=subject
        self._fromUser=fromUser
        self._sqm=sqm
        self._subject=subject
        self._toUser=toUser
    def sendMail(self,filename):
        try:
            with open(os.path.join(rePath,filename),'rb') as f:
                msg=f.read()
        except Exception as e:
            log.logger.exception('open or read file [%s] failed,No such file or directory: %s' % (filename, rePath))
            raise e
        else:
            log.logger.info('open and read file [%s] successed!' %filename)
            message = MIMEMultipart()
            message['from']=self._fromUser
            message['to']=self._toUser
            message['Subject']=self._subject

            message.attach(MIMEText("测试报告","plain","utf-8"))
            att1=MIMEText(msg,'html','utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="%s"'%(filename,)
            message.attach(att1)
            try:
                smtp=smtplib.SMTP()
                smtp.connect(self._server)
                smtp.login(self._fromUser, self._sqm)
            except Exception as e:
                log.logger.exception('connect [%s] server failed or username and password incorrect!' % smtp)
                raise e
            else:
                log.logger.info('email server [%s] login success!' % smtp)
                try:
                    smtp.sendmail(self._fromUser,self._toUser,message.as_string())
                    print('email send ok')
                except Exception as e :
                    log.logger.exception('send email failed!')
                    raise e
                else:
                    log.logger.info("send emial successed")
def getReciver(filename):
        try:
            with open(os.path.join(daPath,filename)) as f:
                msgs=f.readlines()
        except Exception as e:
            log.logger.exception('open or read file [%s] failed,No such file or directory: %s' %(filename, daPath))
            raise e
        else:
            return msgs[-1]
if __name__ == '__main__':

    send=sendEmail('test email',server='smtp.qq.com',fromUser="905949017@qq.com",sqm='uxzznkpfjvwkbbbf',toUser="guch@bankcall.net")
    send.sendMail('/home/gu/PycharmProjects/auto_test/oaTail/report/testReport/test.html')

    # print(getReciver("receiver.txt"))
    # / home / gu / PycharmProjects / auto_test / oaTail / data / testData / receiver.txt



