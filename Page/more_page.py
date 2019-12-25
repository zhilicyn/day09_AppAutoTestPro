from Base.base import Base
from Page.pageElements import PageElements


class MorePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_network_btn(self):
        """点击更多页面移动网络按钮"""
        self.click_ele(PageElements.more_mobile_btn_xpath)
