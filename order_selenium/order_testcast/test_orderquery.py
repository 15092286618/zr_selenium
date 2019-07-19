'''
Created on 2019年7月19日

@author: Vivian
'''
#coding=utf-8
import unittest
from selenium import webdriver
from order_selenium.order_pageobject.OrderQueryPage import OrderQueryPage
from order_selenium.order_pageobject.OrderLoginPage import OrderLoginPage
import time 
from order_selenium.order_testcast.test_base import TestOrderBase


class TestQuery(TestOrderBase): 

    def test_order_query(self):
        #登录
        ord = OrderLoginPage(self.driver,self.url,u'起始页 -订单中心V2- 轮子科技') 
        ord.login(self.username,self.password,1)
        qry = OrderQueryPage(self.driver,self.url,u'起始页 -订单中心V2- 轮子科技')
        qry.open_ordermenu()
        qry.cust_settle_inp('上海易鑫')
        time.sleep(2)
        
        qry.order_number_inp('20190719113656379972A')
        
        time.sleep(2)
        qry.search_btn_click()
        time.sleep(10)
        qry.clear_btn_click()
        time.sleep(2)
        qry.search_btn_click()
        qry.refresh_web()

# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()