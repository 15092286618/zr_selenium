'''
Created on 2019年6月14日

@author: Vivian
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from locust import web
from order_selenium.order_pageobject.BasePage import BasePage


class OrderLoginPage(BasePage):
    '''
#     基础类，用于页面对象的继承
    订单中心登录
    '''
    
#     url = 'http://mallv2-admin-ls.lunztech.cn/Login?ReturnUrl=%2F#/dashboard'
    
    #定位器
    username_inp = (By.NAME,'username')
    password_inp = (By.NAME,'password')
    remember_chk = (By.NAME,'remember')
    submit_btn = (By.CSS_SELECTOR,'.btn.blue.pull-right')
    
    user_id = (By.CSS_SELECTOR,'.username.username-hide-on-mobile.ng-binding')
     
     
    order_menu01 = (By.XPATH,'/html/body/div[3]/div[1]/div/ul/li[4]/a/span[1]')
    order_menu02 = (By.CSS_SELECTOR, 'body > div.page-container > div.page-sidebar-wrapper.ng-scope > div > ul > li.ng-scope.open > ul > li:nth-child(5) > a > span')
     
        
#     def __init__(self,usr,psd,url):
     
    #操作
    #通过继承覆盖（overrding）方法：如果子类和父类的方法名相同，优先用子类自己的方法
    
    #打开网页
    def open(self):
        #调用basepage中的_open打开链接
        self._open(self.url, self.title)
        sleep(5)
    
    #输入用户名
    def input_username(self,username):
        self.driver.find_element(*self.username_inp).clear()
        self.driver.find_element(*self.username_inp).send_keys(username)
    
    #输入密码   
    def input_password(self,password):
        self.driver.find_element(*self.password_inp).clear()
        self.driver.find_element(*self.password_inp).send_keys(password)
    
    #勾选记住密码
    def check_remember(self):
        if self.driver.find_element(*self.remember_chk).is_selected():
            return
            
#         self.driver.find_element(*self.remember_chk).clear()
        self.driver.find_element(*self.remember_chk).click()
        assert self.driver.find_element(*self.remember_chk).is_selected()
        
    #提交，登录
    def button_submit(self):
#         assert self.driver.find_element(*self.submit_btn).enable()
        self.driver.find_element(*self.submit_btn).click()
    
    #登录成功后，页面中的用户ID查找
    def show_userid(self):
        return self.driver.find_element(*self.user_id).is_displayed()
#         return self.find_element(*self.user_id).text

    #登录方法
    def login(self,usr,psd,flag):
        self.open()
        self.input_username(usr)
        self.input_password(psd)
        if flag:
            self.check_remember()
        self.button_submit()


    
        
        
    