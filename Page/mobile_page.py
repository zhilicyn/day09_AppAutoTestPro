from Base.base import Base
from Page.pageElements import PageElements


class MobilePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_first_network_btn(self):
        """移动网络页面点击首选网络类型"""
        self.click_ele(PageElements.mobile_first_network_xpath)

    def click_2G_btn(self):
        """移动网络页面首选网络类型弹窗点击2G"""
        self.click_ele(PageElements.mobile_select_2G_btn_xpath)

    def get_network_result(self):
        """获取首选网络类型修改结果"""
        results = self.search_eles(PageElements.mobile_get_summary_text_ids)
        return [i.text for i in results]
