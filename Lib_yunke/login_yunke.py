from selenium.webdriver.common.action_chains import ActionChains
class Login():
    def user_login(self,driver):
        driver.get('https://www.yunke.com/index.main.login')
        driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[1]/div[2]/input').clear()
        driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[1]/div[2]/input').send_keys('17600117243')
        driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').clear()
        driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').send_keys('117243')
        driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').submit()
    def user_logout(self,driver):
        above = driver.find_element_by_xpath('//*[@id="chick-down-show"]')
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath('//*[@id="sub-menu"]/div/a[5]').click()
        driver.quit()
