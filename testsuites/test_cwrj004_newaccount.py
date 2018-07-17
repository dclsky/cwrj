#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: dcl
# date: 2018/2/6

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.work_page import WorkPage
from pageobjects.cwrj_login_page import LoginPage
import time
from testsuites.test_cwrj001_login import CwrjLogin


class NewAccount(unittest.TestCase):
    """新建账簿"""
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

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        time.sleep(3)
        cls.driver.quit()

    def test_new_account(self):
        """新建账簿"""

        workpage = WorkPage(self.driver)
        workpage.search_account(u'自动化测试客户')
        time.sleep(2)
        workpage.click_custom()
        workpage.account_detail()
