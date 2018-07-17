#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: dcl
# date: 2018/7/13

from framework.base_page import BasePage
from work_page import WorkPage
import time
import os


class ImportAccountPage(BasePage):
    # 账簿管理按钮
    manage_account = "id=>manageAccountBook"

    # 导入账簿按钮
    import_button = "link_text=>导入账簿数据"

    normal_button = "xpath=>//form[@id='accBookForm']//button[contains(text(),'正常导入')]"
    three_button = "xpath=>//form[@id='accBookForm']//button[contains(text(),'三位编码导入')]"

    # 导入确认按钮
    confirm_button = "xpath=>//div[@id='confirmModal']//button[contains(text(),'确认')]"
    cancel_button = "xpath=>//div[@id='confirmModal']//button[contains(text(),'取消')]"

    # 获取导入工具的路径
    import_tool = os.path.dirname(os.path.abspath('.')) + '\\tools\\import.exe'

    # 文件上传成功提示
    import_success = "xpath=>//div[@id='noticeModal']/div[contains(text(),'文件上传成功')]"

    # 开始导入账簿按钮
    start_import = "xpath=>//*[@id='accBookForm']//button[contains(text(),'开始导入')]"

    # 导入成功提示
    import_result = "xpath=>//*[@id='accBookForm']//div[contains(text(),'导入成功')]"

    def click_manage_account(self):
        self.click(self.manage_account)

    def click_import_account(self):
        self.click(self.import_button)

    # 正常导入
    def file_upload(self, filename):
        self.click(self.normal_button)
        time.sleep(3)
        self.click(self.confirm_button)
        time.sleep(3)

        # 导入文件
        print u'开始执行导入文件:'
        os.system('%s %s' % (self.import_tool, filename))
        if self.disappeare('notice-body', u'文件上传成功'):
            return 1

    def import_normal(self):
        self.click(self.start_import)
        if self.disappeare('text-success', u'导入成功'):
            return True

    def click_three_import(self):
        self.click(self.three_button)
