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
        loginpage.type_user('15801224098')  # 调用页面对象中的方法
        loginpage.type_pass('yq111111')
        # logger.info('ceshi')
        cls.driver.find_element_by_id('loginBtn').click()

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        time.sleep(3)
        cls.driver.quit()

    def test_add_custom(self):
        """
        添加新客户
        :return: 
        """

        logger.info('进入客户管理页面')
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@id='frameHeader']/div[3]/div[3]/span").click()

        addpage = AddPage(self.driver)
        addpage.add_custom()
        addpage.custom_detail(u'自动化测试客户')
        self.driver.find_element_by_xpath('//*[@id="promptModal"]//*/button[text()="保存"]').click()
        logger.info("新增客户成功！")
        addpage.get_windows_img()  # 调用基类截图方法

        # table = self.driver.find_element_by_class_name('table')
        # table_rows = table.find_elements_by_tag_name('tr')
        # print u"客户数量：%s"%len(table_rows)
        # # logger.info(len(table_rows))
        # for table_row in table_rows:
        #     a = table_row.find_elements_by_tag_name('td')
        #     logger.info(a[2].text)
        q = self.driver.find_element_by_xpath("//*[@id='frameContent']/div[2]/div[2]/div[2]/span")
        logger.info("客户数量：%s"%len(q))

