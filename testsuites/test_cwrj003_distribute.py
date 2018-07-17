#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: dcl
# date: 2018/2/5

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.custom_manage_page import DisPage
from pageobjects.cwrj_login_page import LoginPage
from framework.logger import Logger
import time

logger = Logger(logger="custom_manage_page").getlog()


class DistributeCustom(unittest.TestCase):
    """分配客户"""
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
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        time.sleep(3)
        cls.driver.quit()

    def test_distri_custom(self):
        """分配客户"""

        logger.info('进入客户管理页面')
        # time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='frameHeader']//span[contains(text(),'客户管理')]").click()
        time.sleep(2)
        logger.info("开始分配客户")

        dispage = DisPage(self.driver)
        dispage.distri_custom()
        dispage.select_account()
        dispage.get_windows_img()

        self.assertTrue(dispage.distri_click())

        dispage.get_windows_img()
        logger.info("分配成功")
