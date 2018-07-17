#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: dcl
# date: 2018/7/13

import unittest
from pageobjects.import_account_page import ImportAccountPage
from pageobjects.work_page import WorkPage
from framework.browser_engine import BrowserEngine
from pageobjects.cwrj_login_page import LoginPage
from pageobjects.import_account_page import ImportAccountPage
import time
from framework.logger import Logger

logger = Logger(logger="BasePage").getlog()


class ImportAccount1(unittest.TestCase):
    """导入账簿"""

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

        # 登录系统
        loginpage = LoginPage(cls.driver)
        loginpage.user_login()
        workpage = WorkPage(cls.driver)
        workpage.search_account(u'自动化测试客户')
        time.sleep(2)
        workpage.enter_account()
        import_account = ImportAccountPage(cls.driver)
        import_account.click_manage_account()
        import_account.click_import_account()
        print '进入账簿导入页面'

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        time.sleep(3)
        cls.driver.quit()

    def test01_normal_upload(self):
        """正常导入-文件上传"""
        importaccountpage = ImportAccountPage(self.driver)
        upload_status = importaccountpage.file_upload("D:\\autotest\\cwrj\\tools\\nbdf.szyqcwgj")
        logger.info('正在上传文件，请稍后...')
        self.assertTrue(upload_status, u'文件上传失败')
        importaccountpage.get_windows_img()
        time.sleep(2)

    def test02_normal_import(self):
        """正常导入-导入"""
        importaccountpage = ImportAccountPage(self.driver)
        logger.info('开始导入账簿，请稍后...')
        import_status = importaccountpage.import_normal()
        self.assertTrue(import_status, u'导入失败')
        importaccountpage.get_windows_img()

if __name__ == '__main__':
    unittest.main()
