# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    username = "id=>account"
    password = "id=>password"
    login_btn = "xpath=>//*[@id='loginBtn']"
    # 找回密码入口
    call_pass = "link_text=>忘记密码"
    # 注册入口
    register = "link_text=>立即注册"

    def type_user(self, text):
        self.type(self.username, text)

    def type_pass(self, text):
        self.type(self.password, text)

    def click_login(self):
        self.click(self.login_btn)

    def call_password(self):
        self.click(self.call_pass)
        self.sleep(2)

    def user_login(self, name='18410937475', passwd='yq111111'):
        self.type_user(name)
        self.type_pass(passwd)
        self.click_login()
