# auto_test
		基于selenium+pyhon3自动化测试基础框架
		目录结构
		├── oaTail
		│   ├── config #配置文件夹
		│   │   ├── config.ini
		│   │   ├── config.py
		│   │   ├── __init__.py
		│   ├── data #数据、参数变量
		│   │   └── testData
		│   │       ├── login.xlsx
		│   ├── __init__.py
		│   ├── report #测试报告以及日志
		│   │   ├── log#日志
		│   │   └── testReport#HTMLTestRunner生成的测试报告
		│   │       ├── report #BeautifulReport生成测试报告
		│   │       ├── test.html
		│   └── test_Case
		│       ├── __init__.py
		│       ├── models #一些共用方法
		│       │   ├── doConfini.py#处理配置文件
		│       │   ├── doExecl.py#处理execl
		│       │   ├── driver.py#基础驱动
		│       │   ├── __init__.py
		│       │   ├── log.py#日志
		│       │   ├── myunittest.py#基础unittest
		│       │   ├── sendEmail.py#发送邮件
		│       │   ├── testReport.py#生成testreport
		│       ├── page_obj #page_obj#
		│       │   ├── base_page.py
		│       │   ├── __init__.py
		│       │   ├── loginPage.py
		│       └── testcase#测试用例
		│           ├── daTest
		│           ├── runner.py
		│           ├── test1.py
		│           └── testLogin.py
		├── packpage#第三方包
		├── packpage.txt
		└── README.md
		这是自己工作中的制作的一个小项目，可以直接拿来用，也可以继续扩展

