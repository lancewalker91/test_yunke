from selenium import webdriver
from Lib_yunke.login_yunke import Login
import unittest
class MyTest(unittest.TestCase):
    '''云课登录测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    def test_login(self):
        '''调用login_yunke'''
        driver = self.driver
        Login().user_login(driver)
        text = driver.find_element_by_xpath('//*[@id="topnav"]/div/ul/li[3]/a').text
        self.assertEqual(text, '机构管理')
    def tearDown(self):
        driver = self.driver
        Login().user_logout(driver)
if __name__ =='__main__':
    unittest.main()
