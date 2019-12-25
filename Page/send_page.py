from appium.webdriver.common.touch_action import TouchAction

from Base.base import Base
from Page.pageElements import PageElements


class SendPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def input_phone_num(self,phone_num):
        """输入手机号"""
        self.send_ele(PageElements.new_sms_phone_num_id, phone_num)

    def send_sms(self,msg):
        """编辑短信和发送短信"""
        self.send_ele(PageElements.sms_input_id,msg)
        self.click_ele(PageElements.sms_send_btn_id)

    def delete_msg(self,msg):
        """删除指定信息的短信"""
        ele = self.search_ele((PageElements.sms_delete_msg_xpath[0],PageElements.sms_delete_msg_xpath[1].format(msg)))
        TouchAction(self.driver).long_press(ele).release().perform()
        self.click_ele(PageElements.sms_delete_btn_xpath)
        self.click_ele(PageElements.sms_delete_btn_id)

    def get_msg_list(self):
        """获取短信列表信息并返回"""
        results = self.search_eles(PageElements.sms_list_id)
        return [i.text for i in results]