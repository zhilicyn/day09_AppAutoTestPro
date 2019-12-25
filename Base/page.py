from Page.mobile_page import MobilePage
from Page.more_page import MorePage
from Page.search_page import SearchPage
from Page.send_page import SendPage
from Page.setting_page import SettingPage
from Page.sms_page import SMSPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    def get_setting_page(self):
        """返回设置页面实例化对象"""
        return SettingPage(self.driver)

    def get_search_page(self):
        """返回搜索页面实例化对象"""
        return SearchPage(self.driver)

    def get_more_page(self):
        """返回更多页面实例化界面"""
        return MorePage(self.driver)

    def get_mobile_page(self):
        """返回移动网络页面实例化对象"""
        return  MobilePage(self.driver)

    def get_sms_page(self):
        """返回短信页面实例化对象"""
        return SMSPage(self.driver)

    def get_send_page(self):
        """返回发送短信页面实例化对象"""
        return SendPage(self.driver)
