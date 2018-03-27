#-*- coding:utf-8 -*-
from selenium import webdriver
from Lib_yunke.login_yunke import Login
import unittest
from time import sleep
class MyTest(unittest.TestCase):
    '''上传图片测试'''
    def setUp(self):
        self.driver = webdriver.Firefox( )
        self.driver.implicitly_wait(10)
        Login().user_login(self.driver)
    def test_upload_img(self):
        driver = self.driver
        driver.get('https://litao.yunke.com/org.course.setimg.56032')
        sleep(10)
        driver.find_element_by_css_selector('html body div#p1c94840u42n31el01hr61t2o19ta0_html5_container.plupload.html5 input#p1c94840u42n31el01hr61t2o19ta0_html5').click()
    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()
