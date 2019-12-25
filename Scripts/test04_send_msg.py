import time

import pytest,sys,os
sys.path.append(os.getcwd())

from Base.getDriver import get_android_driver
from Base.page import Page


class TestSendMessage:
    def setup_class(self):
        # 初始化driver
        # com.android.mms/.ui.ComposeMessageActivity
        self.driver = get_android_driver("com.android.mms",".ui.ConversationList")
        # 实例化Page类
        self.page = Page(self.driver)

    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.fixture(autouse=True,scope="class")
    def goto_new_msg(self):
        # 点击新建按钮
        self.page.get_sms_page().click_add_btn()
        # 输入手机号
        self.page.get_send_page().input_phone_num("18712345678")

    @pytest.mark.parametrize("msg",[("我有故人抱剑去","斩尽春风未肯归","知离吖")])
    def test_send_msg(self,msg):
        print(msg)
        # 发送短信
        for i in msg:
            self.page.get_send_page().send_sms(i)
        # 删除指定短信
        self.page.get_send_page().delete_msg(msg[2])
        # 获取短信列表信息
        result = self.page.get_send_page().get_msg_list()
        # 断言
        assert msg[2] not in result
