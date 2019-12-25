import time

import pytest, sys, os

# 添加自定义路径到python的搜索路径
sys.path.append(os.getcwd())

from Base.getDriver import get_android_driver
from Page.search_page import SearchPage


class TestSearch:
    def setup_class(self):
        # com.android.settings/.Settings
        # 创建驱动对象
        self.driver = get_android_driver("com.android.settings", ".Settings")
        self.search_page = SearchPage(self.driver)

    def teardown_class(self):
        # 页面等待
        time.sleep(3)
        # 关闭驱动对象
        self.driver.quit()

    @pytest.fixture(autouse=True, scope="class")
    def goto_search(self):
        """点击搜索按钮"""
        self.search_page.click_search_btn()

    @pytest.mark.parametrize("search_data,exp_data", [("1", "休眠"), ("m", "MAC地址"), ("w", "WPS按钮")])
    def test01_search(self, search_data, exp_data):
        """
        测试方法
        :param search_data: 搜索内容
        :param exp_data: 预期包含结果
        :return:
        """
        # 搜索框输入搜索内容
        self.search_page.search_text(search_data)
        # 获取搜索结果
        result = self.search_page.get_search_result()
        # 断言
        print("\n搜索内容:{},预期结果:{}".format(search_data, exp_data), end="")
        assert exp_data in result


if __name__ == '__main__':
    pytest.main()
