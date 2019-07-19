'''
Created on 2019年6月14日

@author: Vivian
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    '''
    BasePage封装所有页面都公用的方法，例如driver,url,findelement等
    '''
    
    #初始化driver url  title
    #实例化BasePage类时，最先执行的就是__int__方法，该方法的入参，其实就是BasePage类的入参
    #__int__方法不能有返回值，只能返回none
    #self指实例本身，相较于类page而言
    def __init__(self, driver, url, title):
        self.driver = driver
        self.url = url
        self.title = title
    
    #通过页面的title属性，断言进入的页面是否正确
    def on_page(self, title):
#         assert title.is_displayed()
#         return True 
          return (title in self.driver.title)
    
    #打开页面，并校验页面链接是否加载正确
    #以单下划线_ 开头的方法，在使用import * 时，该方法不会被导入，保证该方法为类私有
    def _open(self,url,title):
        #使用get打开访问链接的地址
        self.driver.get(url)
        self.driver.maximize_window()
        #使用assert进行校验，打开的窗口中，显示的登录用户是否与配置的一致，调用on_page()方法
        assert self.on_page(title), u'打开%s页面成功'%url
        
    #定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.url, self.title)




