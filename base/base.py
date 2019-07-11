from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化浏览器对象
    def __init__(self,driver):
        self.driver=driver
    # 元素定位
    def base_find(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 输入
    def base_input(self,loc,value):
        el=self.base_find(loc)
        el.clear()
        el.send_keys(value)
    # 点击
    def base_click(self,loc):
        self.base_find(loc).click()
    # 截图
    def base_img(self,file):
        self.driver.get_screenshot_as_file(file)


    # 获取断言文本
    # def base_text(self,loc):
    #     self.base_find(loc)