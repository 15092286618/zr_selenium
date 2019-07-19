'''
Created on 2019年7月19日

@author: Vivian
'''
import unittest
from selenium import webdriver


class TestOrderBase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('111111')
    
    @classmethod
    def tearDownClass(self):
    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('222222')


    def setUp(self):
#         self.driver = webdriver.Chrome()  #可以，没问题
        self.driver = webdriver.Firefox()  #可以，没问题。将对于的driver.exe放在python的安装目录下即可
        self.driver.implicitly_wait(30)
        self.url = 'http://mallv2-admin-ls.lunztech.cn/Login?ReturnUrl=%2F#/dashboard'
        self.title = u'起始页 -订单中心V2- 轮子科技'
        self.username = 'wangxiaowen'
        self.password = '654321' 

        
    def tearDown(self):
        self.driver.quit()


# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()