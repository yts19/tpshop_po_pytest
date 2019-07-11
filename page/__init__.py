"""元素定位"""
from selenium.webdriver.common.by import By

click_login_link_btu=By.LINK_TEXT,"登录"
input_phone=By.ID,"username"
input_pwd=By.ID, "password"
input_code=By.ID,"verify_code"

# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 异常提示信息
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# 异常提示框确定
clicK_comfirm = By.CSS_SELECTOR, ".layui-layer-btn0"
# 获取昵称
login_nickname = By.CSS_SELECTOR, ".userinfo"
# 安全退出
clicK_logout = By.LINK_TEXT, "安全退出"
# 服务器地址
url = "http://localhost"
