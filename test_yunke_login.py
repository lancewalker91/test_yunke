from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Lib_yunke.login_yunke import Login
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    def test_login(self):
        driver = self.driver
        Login().user_login(driver)
        text = driver.find_element_by_xpath('//*[@id="topnav"]/div/ul/li[3]/a').text
        self.assertEqual(text, '机构管理')
    def tearDown(self):
        driver = self.driver
        Login().user_logout(driver)
if __name__ =='__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(MyTest('test_login'))
    fp = open(r'C:\Users\Administrator\Desktop\云课登录测试报告.html','wb')
    runner = HTMLTestRunner(stream=fp,title='云课登录测试报告',description='用例执行情况：')
    runner.run(testunit)
    fp.close()