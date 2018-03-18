import time
from HTMLTestRunner import HTMLTestRunner
import unittest
test_dir = r'C:\Users\16033\Desktop\test_yunke'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open(r'C:\Users\16033\Desktop' + '\\' + now + '云课登录测试报告.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='云课UI自动化测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()