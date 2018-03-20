from selenium import webdriver
from Lib_yunke.login_yunke import Login
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

class MyTest(unittest.TestCase):
    '''云课建课测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        Login().user_login(self.driver)
    def test_buildcourse(self):
        '''建课流程编写'''
        driver = self.driver
        driver.get('https://yunkelearning.yunke.com/user.org.course')
        driver.find_element_by_xpath('//*[@id="goCreateCourse"]').click()
        time.sleep(1)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.find_element_by_xpath('/html/body/section/div/div[1]/div/div/div/div/div[1]/a').click()
        driver.find_element_by_id('get-courseInfo-title').send_keys('自动化建课测试')
        driver.find_element_by_xpath('//*[@id="get-firstCate-btn"]/cite').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="get-cate"]/dd[1]/a').click()
        driver.find_element_by_xpath('//*[@id="add-secondCate"]/cite').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="get-cate-class"]/dd[2]/a').click()
        driver.find_element_by_xpath('//*[@id="add-thirdCate"]/cite').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="get-cate-name"]/dd[2]/a').click()
        driver.find_element_by_xpath('//*[@id="teachers-cent"]/div[1]').click()
        driver.find_element_by_xpath('//*[@id="multiple-left"]/li[1]').click()
        driver.find_element_by_xpath('//*[@id="add-btn"]').click()
        driver.find_element_by_xpath('//*[@id="course_add"]').click()
        driver.find_element_by_xpath('//*[@id="add-course-info-btn"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="img_p_label"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="uploadImg"]').click()
        os.system(r'C:\Users\Administrator\Desktop\test_yunke\uploadimg.exe')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="saveImg"]').click()
        driver.find_element_by_xpath('/html/body/section[1]/div/div/section/ul/li[5]/button').click()
        driver.find_element_by_xpath('//*[@id="save-btn"]').click()
        driver.find_element_by_xpath('//*[@id="add-single-class"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div/div[1]/input').send_keys('测试')
        driver.find_element_by_css_selector('#start-one-time').click()
        time.sleep(0.5)
        driver.execute_script("$('.xdsoft_datetimepicker:visible .xdsoft_time.xdsoft_current').click()")
        driver.find_element_by_css_selector('#end-one-time').click()
        time.sleep(0.5)
        driver.execute_script("$('.xdsoft_datetimepicker:visible .xdsoft_time.xdsoft_current').click()")
        driver.find_element_by_css_selector('body').click()
        driver.find_element_by_xpath('//*[@id="add-plan-btn"]').click()
        time.sleep(2)
        driver.refresh()
        driver.find_element_by_xpath('//*[@id="create-success"]').click()
        time.sleep(600)
        driver.find_element_by_link_text('自动化建课测试').click()
        time.sleep(1)
        windows2 = driver.window_handles
        driver.switch_to.window(windows2[-1])
        text = driver.find_element_by_xpath('/html/body/section/div/div/section[2]/div[1]/div/div/div[2]/ul/li/a/dl/dd').text
        self.assertEqual(text,'测试')
    def tearDown(self):
        driver = self.driver
        windows3 = driver.window_handles
        driver.switch_to.window(windows3[-2])
        driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/ul/li[1]/div[4]/p/a[1]').click()
        driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()
        driver.get('https://www.yunke.com')
        Login().user_logout(driver)
if __name__ == '__main__':
    unittest.main()



