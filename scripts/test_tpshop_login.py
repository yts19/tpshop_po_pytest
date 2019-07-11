import sys,os
sys.path.append(os.getcwd())
import pytest

from base.base import Base
from page.page_tp_login import PageLogin
from tool.get_data import data
from tool.get_driver import GetDriver
from tool.get_log import GetLog


def data_get():
    data()
    mylist = []
    for i in data():
        mylist.append(tuple(i.strip().split(',')))
    return mylist[1:]



class TestLogin():
    # 初始化

    def setup_class(self):
        self.driver = GetDriver.get_driver()
        self.log=GetLog.get_loggin()
        self.page_tpshop=PageLogin(self.driver)

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()
    # 测试方法
    @pytest.mark.parametrize("phone,pwd,code,expect,mark",data_get())
    def test_login(self,phone,pwd,code,expect,mark):


        # 输入数据

        # 判断是否登录成功
        if mark == "true":
            self.page_tpshop.page_click_login_link_btn()
            self.page_tpshop.page_login_proxy(phone, pwd, code)
            try:
                assert expect==self.page_tpshop.page_nickname()

            except Exception as e:
                print(e)
                # 日志信息
                self.log.error(e)
                # 截图
                # self.page_tpshop.page_get_img('./img/login_{}.png'.format("%H%M%S"))
                raise
            finally:

                self.page_tpshop.page_click_login_out()
                self.page_tpshop.page_click_login_link_btn()

        else:
            self.page_tpshop.page_login_proxy(phone, pwd, code)

            try:

                assert expect == self.page_tpshop.page_get_text()

            except Exception as e:
                print(e)

                self.driver.get_screenshot_as_file('./img/login.png')
                self.log.error(e)
                raise
            finally:
                self.page_tpshop.page_click_confirm_brn()


