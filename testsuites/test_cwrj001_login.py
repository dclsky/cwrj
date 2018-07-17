# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.cwrj_login_page import LoginPage
from framework.logger import Logger

logger = Logger(logger="cwrj_login_page").getlog()


class CwrjLogin(unittest.TestCase):
    """登录测试"""
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        time.sleep(3)
        cls.driver.quit()

    def test_alogin(self):
        """正常登录"""
        loginpage = LoginPage(self.driver)
        loginpage.user_login()

        self.driver.get_screenshot_as_png()

        loginpage.get_windows_img()  # 调用基类截图方法
        self.assertEqual(u'易桥财务管家', loginpage.get_page_title())  # 调用页面对象继承基类中的获取页面标题方法
        logger.info("登录成功")
        # except Exception as e:
        #     print ('Test Fail.', e)

    # def test_search2(self):
    #     homepage = HomePage(self.driver)
    #     homepage.type_search('python')  # 调用页面对象中的方法
    #     homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
    #     time.sleep(2)
    #     homepage.get_windows_img()  # 调用基类截图方法

if __name__ == '__main__':
    unittest.main()

