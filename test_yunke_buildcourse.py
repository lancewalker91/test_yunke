from selenium import webdriver
from Lib_yunke.login_yunke import Login
import unittest
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.implicitly_wait(30)
Login().user_login(driver)
driver.get('https://yunkelearning.yunke.com/org.course.add.1')
driver.find_element_by_id('get-courseInfo-title').send_keys('自动化测试')
driver.find_element_by_xpath('/html/body/section[1]/div/div/section/div/section/div[1]/div[2]/div[1]/cite/span[1]').click()
driver.find_element_by_link_text('生活/兴趣').click()
'''driver.get('https://yunkelearning.yunke.com/user.org.course')
current_handle = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="goCreateCourse"]').click()
all_hanldes = driver.window_handles
for handle in all_hanldes:
    if handle != current_handle:
        driver.switch_to_.window(handle)
        double_click = driver.find_element_by_link_text('直播课')
        ActionChains(driver).double_click(double_click).perform()

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        Login().user_login(self.driver)
    def test_build(self):
        driver = self.driver
        driver.get('https://yunkelearning.yunke.com/org.course.add.1')
        driver.find_element_by_id('get-courseInfo-title').send_keys('自动化测试')
        driver.find_element_by_xpath('').click()'''