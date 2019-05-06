# -*- coding: utf-8 -*-
import os
from oaTail.test_Case.models.doConfini import doConfini
#获取当前路径
currPath=os.path.split(os.path.realpath(__file__))[0]
print(os.path.split(os.path.abspath(__file__))[0])
#
readConfig=doConfini()
#读取配置文件
confpath=os.path.join(currPath,'config.ini')
absPath=readConfig.getConfValue(confpath,'project','project_path')
#日志路径
logPath=os.path.join(absPath,'oaTail','report','log')
#用例路径
tcPath=os.path.join(absPath,"oaTail",'test_Case','testcase')
#报告路径
rePath=os.path.join(absPath,"oaTail",'report','testReport')
#截图路径
imPassPath=os.path.join(absPath,"oaTail",'report','image','pass')
#错误截图路径
imFailPath=os.path.join(absPath,"oaTail",'report','image','fail')
#测试数据路径
daPath=os.path.join(absPath,"oaTail",'data','testData')
