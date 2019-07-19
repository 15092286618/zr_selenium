'''
Created on 2019年6月19日

@author: Vivian
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from locust import web
from order_selenium.order_pageobject.BasePage import BasePage


class OrderQueryPage(BasePage):
    '''
   订单中心查询
    '''
   
    cust_settle = (By.CSS_SELECTOR,"[data-ng-model='queryModel.CustSettleName']")
#     cust_settle = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div[1]/div[1]/div[2]/input')
    order_number = (By.CSS_SELECTOR,"[data-ng-model='queryModel.OrderNo']")
    
    search_btn = (By.CSS_SELECTOR,"[ng-enter='search()'][ng-click='search()']")
    clear_btn = (By.CSS_SELECTOR,'[class="btn default"][ng-click="clear()"]')
    balance_type_select = (By.CSS_SELECTOR,'[ng-model="queryModel.BalanceType"][ng-options="m.Value as m.Text for m in balanceTypeList"]')
    #balance_type_select_01= 
    
    order_menu01 = (By.XPATH,'/html/body/div[3]/div[1]/div/ul/li[4]/a/span[1]')
    order_menu02 = (By.CSS_SELECTOR, 'body > div.page-container > div.page-sidebar-wrapper.ng-scope > div > ul > li.ng-scope.open > ul > li:nth-child(5) > a > span')

    refresh_btn = (By.CSS_SELECTOR,'.btn.btn-fit-height.grey-salt')
    
    #打开【订单-订单管理】菜单
    def open_ordermenu(self):
        self.driver.find_element(*self.order_menu01).is_displayed()
        self.driver.find_element(*self.order_menu01).click()
        sleep(5)
        self.driver.find_element(*self.order_menu02).is_displayed()
        self.driver.find_element(*self.order_menu02).click()
        sleep(5)
        
    #输入结算单位
    def cust_settle_inp(self,str):
        self.driver.find_element(*self.cust_settle).clear()
        self.driver.find_element(*self.cust_settle).send_keys(str)
#         cust_settle=self.driver.find_element_by_css_selector("body > div.page-container > div.page-content-wrapper > div > div > div.row.ng-scope > div:nth-child(1) > div > div.portlet-body.form > form > div.form-body > div:nth-child(3) > div:nth-child(4) > select")
#         cust_settle.send_keys(self.str)
    
    #输入订单号 
    def order_number_inp(self,str):
        self.driver.find_element(*self.order_number).clear()
        self.driver.find_element(*self.order_number).send_keys(str)
    
    #查询   
    def search_btn_click(self):
#        assert self.driver.find_element(self.search_btn).enabled()
        self.driver.find_element(*self.search_btn).click()
        sleep(2)
    
    #清除
    def clear_btn_click(self):
        self.driver.find_element(*self.clear_btn).click()      
        sleep(2)

    #点击刷新
    def refresh_web(self):
        self.driver.find_element(*self.refresh_btn).click()
        sleep(2)
        
        
    #模拟键盘enter操作
    def enter_btn(self):
        self.driver.press_key(66)
        
        
        