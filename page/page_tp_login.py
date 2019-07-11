import page
from base.base import Base


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link_btn(self):
        self.base_click(page.click_login_link_btu)

    # 输入手机号
    def page_input_phone(self,phone):
        self.base_input(page.input_phone,phone)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.input_pwd,pwd)
    # 输入验证码
    def page_input_code(self,code):
        self.base_input(page.input_code,code)
    # 点击退出
    def page_click_login_out(self):
        self.base_click(page.clicK_logout)
    def page_click_confirm_brn(self):
        self.base_click(page.clicK_comfirm)
    # 获取截图
    def page_get_img(self,flie):
        self.base_img(flie)
    # 点击登录
    def page_click_btn(self):
        self.base_click(page.login_btn)
    # 获取文本
    def page_get_text(self):
        return self.base_find(page.login_err_info).text
    # 获取昵称
    def page_nickname(self):
        return self.base_find(page.login_nickname).text
    # 登录操作
    def page_login_proxy(self,phone,pwd,code):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_input_code(code)
        self.page_click_btn()
