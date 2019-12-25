import time

import pytest, sys, os

# 添加自定义路径到python搜索路径
from Base.getDriver import get_android_driver
from Base.page import Page

sys.path.append(os.getcwd())



class TestSetNetwork:
    def setup_class(self):
        # com.android.settings /.Settings
        # 初始化driver
        self.driver = get_android_driver("com.android.settings", ".Settings")
        self.page = Page(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.fixture(autouse=True, scope="class")
    def goto_set_network(self):
        """进入移动网络设置页面"""
        # 点击更多
        self.page.get_setting_page().click_more_btn()
        # 点击移动网络设置
        self.page.get_more_page().click_network_btn()

    @pytest.mark.parametrize("expect", ['2G'])
    def test01_set_first_network(self, expect):
        """测试方法"""
        # 点击首选网络类型
        self.page.get_mobile_page().click_first_network_btn()
        # 选择2G
        self.page.get_mobile_page().click_2G_btn()
        # 获取修改结果
        results = self.page.get_mobile_page().get_network_result()
        # 断言
        print("\n预期结果:首选网络类型为{}".format(expect))
        assert expect in results
