#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: dcl
# date: 2018/2/5

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.custom_manage_page import DisPage
from pageobjects.cwrj_login_page import LoginPage
from framework.base_page import BasePage
from framework.logger import Logger
import time

logger = Logger(logger="custom_manage_page").getlog()


class DistributeCustom(unittest.TestCase):
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

    def test_distri_custom(self):
        """
                分配客户
                :return: 
        """

        logger.info('进入客户管理页面')
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='frameHeader']/div[3]/div[3]/span").click()
        time.sleep(2)
        logger.info("开始分配客户")

        dispage = DisPage(self.driver)
        dispage.distri_custom()
        dispage.select_account()
        dispage.get_windows_img()
        # self.driver.find_element_by_xpath("//*[@id='referModal']/div/div/div[2]/div[2]/table/tbody/tr/td[3]").click()
        # dispage.get_windows_img()
        self.driver.find_element_by_xpath("//*[@id='customerAssignForm']/div[4]/button[1]").click()
        logger.info("分配成功")
