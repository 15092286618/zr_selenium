'''
Created on 2019年6月14日

@author: Vivian
'''

#coding=utf-8
import unittest
from selenium import webdriver
from order_selenium.order_pageobject.OrderQueryPage import OrderQueryPage
from order_selenium.order_pageobject.OrderLoginPage import OrderLoginPage
from order_selenium.order_testcast.test_orderlogin import TestLogin
from order_selenium.order_testcast.test_orderquery import TestQuery
import time
from order_selenium.common.HTMLTestRunner import HTMLTestRunner 
from order_selenium.common.SendMail import send_mail
from lxml.html._diffcommand import description
from order_selenium.order_testcast.test_base import TestOrderBase



# class TestOrderMain(TestOrderBase):
#    
#     @unittest.skip('用例01无条件跳过')
#     def test_01(self):
#         print('01')
#     
#     @unittest.skipIf(2>1,'条件为True,用例02跳过') 
#     def test_02(self):
#         print('02')
#     
#     @unittest.skipUnless(2<1,'条件为False,用例03跳过')
#     def test_03(self):
#         print('03')
        

         
if __name__ == "__main__":

#     unittest.main()
    
    #创建文件，搜集测试结果，生成.html测试报告
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = '../report/webuireport_' + now + '.html' 
#     ftp = open(filename,'wb+')
    ftp = open(filename,'wb+')
    #构造测试集
    suite = unittest.TestSuite()
 #   suite.addTest(TestLogin('test_order_login'))
    suite.addTest(TestQuery('test_order_query'))
    
#     description = '''
#                   注意：
#                   Pass为测试执行通过，Fail为测试执行失败，Error为测试脚本有误
#                   '''

    #创建对象，执行测试集，关闭文件，发送邮件
    runner = HTMLTestRunner(
        stream=ftp,
        verbosity=1,
        title='订单中心WebUI自动化测试报告',
        description='注意：Pass为测试执行通过，Fail为测试执行失败，Error为测试脚本有误'
        )
    
    runner.run(suite)
    ftp.close()
    send_mail(filename)