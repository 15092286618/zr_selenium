'''
Created on 2019年6月19日

@author: Vivian
'''
#coding=utf-8
import unittest
from selenium import webdriver
from order_selenium.order_pageobject.OrderLoginPage import OrderLoginPage
import time 
from order_selenium.order_testcast.test_base import TestOrderBase

class TestLogin(TestOrderBase):

    def test_order_login(self):
        #调用orderpage类对象
        order_lgn = OrderLoginPage(self.driver,self.url,u'起始页 -订单中心V2- 轮子科技') #title可以用其中的任意一串字符串
        #打开页面
        order_lgn.open()
        #调用用户名输入方法
        time.sleep(2)
        order_lgn.input_username(self.username)
        #调用密码输入方法
        order_lgn.input_password(self.password)
        #调用记住密码选中方法
        time.sleep(2)
        order_lgn.check_remember()
        #调用点击登录方法
        time.sleep(2)
        order_lgn.button_submit()
        #验证登录成功
        time.sleep(10)
        order_lgn.show_userid()
        time.sleep(2)
        #退出并关闭浏览器
        self.driver.quit()


# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()