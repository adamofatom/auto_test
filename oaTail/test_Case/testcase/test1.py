# -*- coding: utf-8 -*-
import unittest
from oaTail.test_Case.models.doExecl import readExcel
import ddt

read = readExcel('oa.xlsx', 'login')
data=read.get_data()
@ddt.ddt
class MyTestCase(unittest.TestCase):

    @ddt.data(*data)
    @ddt.unpack
    def test_something(self,root,psswd):
         self.assertEqual(root,psswd)


if __name__ == '__main__':
    unittest.main()

