from Base.base import Base
from Page.pageElements import PageElements


class SMSPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_add_btn(self):
        """点击新建短信按钮"""
        self.click_ele(PageElements.sms_add_btn_id)