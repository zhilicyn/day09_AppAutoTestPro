from selenium.webdriver.common.by import By

from Base.base import Base


class SearchPage:
    def __init__(self, driver):
        # 实例化Base
        self.base = Base(driver)
        # 搜索按钮
        self.search_btn = (By.ID, "com.android.settings:id/search")
        # 输入框
        self.search_input = (By.ID, "android:id/search_src_text")
        # 搜索结果
        self.search_result = (By.ID, "com.android.settings:id/title")

    def click_search_btn(self):
        """点击搜索按钮"""
        self.base.click_ele(self.search_btn)

    def search_text(self, text):
        """输入搜索内容"""
        self.base.send_ele(self.search_input, text)

    def get_search_result(self):
        """获取搜索结果"""
        results = self.base.search_eles(self.search_result)
        return [i.text for i in results]
