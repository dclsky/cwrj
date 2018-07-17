# coding=utf-8
from framework.base_page import BasePage


class AddPage(BasePage):
    # 新增客户
    add_button = "xpath=>//*[@id='frameContent']/div[2]/div[1]/button[1]"
    # 客户详细信息：

    # 客户名称
    custom_name = "xpath=>//*[@id='customerForm']/div[2]/input"
    # 定位纳税人类型
    custom_type = "xpath=>//*[@id='customerForm']/div[3]/select"
    # 纳税人类型:小规模纳税人
    custom_type_value = "SMALL"
    # 保存
    save = 'xpath=>//*[@id="promptModal"]//*/button[text()="保存"]'

    # save_success_loc = 'id=>noticeModal'

    def add_custom(self):
        self.click(self.add_button)
        self.sleep(3)

    def custom_detail(self, text):
        self.type(self.custom_name, text)
        self.select(self.custom_type, self.custom_type_value)

    def custom_save(self):
        self.click(self.save)
        # 判断是否保存成功
        if self.disappeare(u'保存成功'):
            return 1


class DisPage(BasePage):
    # 分配客户到会计
    distribute_button = "xpath=>//*[@id='frameContent']/div[2]/div[2]/table/tbody/tr[1]/td[8]/button[2]"

    # 分配弹窗:
    # 选择记账会计
    # distri_account = "id=>//*[@id='accountantSelector']"
    distri_account = "xpath=>//*[@id='accountantSelector']"
    # accountant = "xpath=>//*[@placehoder='用户名／姓名／手机号／邮箱，按回车查询']"
    accountant = "xpath=>//*[@id='referModal']/div/div/div[2]/div[1]/div/input"
    select_user = "xpath=>//*[@id='referModal']/div/div/div[2]/div[2]/table/tbody/tr"
    # 分配按钮
    distri_button = "xpath=>//*[@id='customerAssignForm']/div[4]/button[1]"

    def distri_custom(self):
        self.click(self.distribute_button)
        self.sleep(2)

    # 选择要分配的记账会计
    def select_account(self):
        self.click(self.distri_account)
        self.clear(self.accountant)
        self.type(self.accountant, '18410937475')
        self.enter(self.accountant)
        self.sleep(2)
        self.click(self.select_user)

    # 点击分配按钮，进行分配
    def distri_click(self):
        self.click(self.distri_button)
        if self.disappeare('notice-body', u'成功'):
            return 1
