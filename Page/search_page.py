from selenium.webdriver.common.by import By

from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):
    def __init__(self, driver):
        # 初始化Base类的init方法
        Base.__init__(self, driver)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(PageElements.search_btn)

    def search_text(self, text):
        """输入搜索内容"""
        self.send_ele(PageElements.search_input, text)

    def get_search_result(self):
        """获取搜索结果"""
        results = self.search_eles(PageElements.search_result)
        return [i.text for i in results]
