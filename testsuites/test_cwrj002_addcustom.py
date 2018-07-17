#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: dcl
# date: 2017/12/11

import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.work_page import WorkPage
from pageobjects.custom_manage_page import AddPage
from pageobjects.cwrj_login_page import LoginPage
from framework.logger import Logger

logger = Logger(logger="custom_manage_page").getlog()


class AddCustom(unittest.TestCase):
    """添加客户"""
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

    def test_add_custom(self):
        """添加新客户"""

        logger.info('进入客户管理页面')
        workpage = WorkPage(self.driver)
        workpage.enter_custom()

        addpage = AddPage(self.driver)
        addpage.add_custom()
        addpage.custom_detail(u'自动化测试客户')
        result = addpage.custom_save()
        self.assertTrue(result), u'保存失败'

        # self.driver.find_element_by_xpath('//*[@id="promptModal"]//*/button[text()="保存"]').click()
        logger.info("新增客户成功！")
        addpage.get_windows_img()  # 调用基类截图方法
