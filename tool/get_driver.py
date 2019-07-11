import page
from selenium import webdriver


class GetDriver:
    # 获取driver
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None