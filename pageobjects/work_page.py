# coding=utf-8
from framework.base_page import BasePage


class WorkPage(BasePage):
    # 新建账簿
    search_custom = "xpath=>//*[@placeholder='请输入客户名称，按回车键查询']"
    new_account = "xpath=>//*[@id='frameContent']/div[2]/div[2]/div[1]/div/div[1]/div[6]/button[1]"

    def enter_account(self, custom_name):
        self.type(self.search_custom, custom_name)
        self.enter(self.search_custom)

    def click_new(self):
        self.click(self.new_account)

    # 进入账簿
    work_custom = "xpath=>//*[@id='frameHeader']/div[3]/div[3]/span"

    def click_custom(self):
        self.click(self.new_account)
        self.sleep(2)

    # 填写账簿信息
    # 账簿名称
    # name = "xpath=>//*[@id='accountBookNameInput']"
    # 选择会计制度
    account_system = "xpath=>//*[@id='accBookForm']/div[2]/select"
    # 小企业会计准则
    account_value = "1"
    # 选择建账月份
    month = "xpath=>//*[@id='accountBookDate']"
    month_value = "xpath=>//*[@class='datepicker-months']/table/tbody/tr/td/span[1]"
    # 保存
    account_save = "xpath=>//*[@id='accBookForm']//button[contains(text(),'保存')]"

    def account_detail(self):
        # self.type(self.name, account_name)
        self.select(self.account_system, self.account_value)
        self.click(self.month)
        self.click(self.month_value)
        self.click(self.account_save)
