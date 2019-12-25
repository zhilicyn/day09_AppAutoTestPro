from selenium.webdriver.common.by import By


class PageElements:
    """管理页面元素类"""

    """搜索页面元素"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")

    """设置页面"""
    # WLAN
    setting_wlan_btn_xpath = (By.XPATH, "//*[contains(@text,'WLAN')]")
    # 更多
    setting_more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")
    # 显示
    setting_display_btn_xpath = (By.XPATH, "//*[contains(@text,'显示')]")
    # 提示音和通知
    setting_notification_btn_xpath = (By.XPATH, "//*[contains(@text,'通知')]")
    # 存储
    setting_save_btn_xpath = (By.XPATH, "//*[contains(@text,'存储')]")
    # 电池
    setting_battery_btn_xpath = (By.XPATH, "//*[contains(@text,'电池')]")
    # 应用
    setting_application_btn_xpath = (By.XPATH, "//*[contains(@text,'应用')]")
    # 用户
    setting_user_btn_xpath = (By.XPATH, "//*[contains(@text,'用户')]")
    # 位置信息
    setting_location_btn_xpath = (By.XPATH, "//*[contains(@text,'位置信息')]")
    # 安全
    setting_safety_btn_xpath = (By.XPATH, "//*[contains(@text,'安全')]")
    # 帐户
    setting_account_btn_xpath = (By.XPATH, "//*[contains(@text,'帐户')]")
    # 语言和输入法
    setting_language_btn_xpath = (By.XPATH, "//*[contains(@text,'语言和输入法')]")
    # 备份和重置
    setting_backup_btn_xpath = (By.XPATH, "//*[contains(@text,'备份')]")
    # 日期和时间
    setting_time_btn_xpath = (By.XPATH, "//*[contains(@text,'日期和时间')]")
    # 无障碍
    setting_accessibility_btn_xpath = (By.XPATH, "//*[contains(@text,'无障碍')]")
    setting_print_btn_xpath = (By.XPATH, "//*[contains(@text,'打印')]")
    # 关于手机
    setting_mobile_btn_xpath = (By.XPATH, "//*[contains(@text,'关于手机')]")



    """更多页面"""
    # 飞行模式
    # more_mobile_btn_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")
    # 移动网络
    more_mobile_btn_xpath = (By.XPATH, "//*[contains(@text,'移动网络  ')]")


    """移动网络设置页面"""
    # 首选网络类型
    mobile_first_network_xpath = (By.XPATH, "//*[contains(@text,'首选网络')]")
    # 2G
    mobile_select_2G_btn_xpath = (By.XPATH, "//*[contains(@text,'2G')]")
    # 获取当前页面所有的summary信息
    mobile_get_summary_text_ids = (By.ID, "android:id/summary")


    """短信页面"""
    # 新建短信按钮
    sms_add_btn_id = (By.ID,"com.android.mms:id/action_compose_new")


    """新信息页面"""
    # 接收者输入框
    new_sms_phone_num_id = (By.ID,"com.android.mms:id/recipients_editor")
    # 信息输入框
    sms_input_id = (By.ID,"com.android.mms:id/embedded_text_editor")
    # 发送按钮
    sms_send_btn_id = (By.ID,"com.android.mms:id/send_button_sms")
    # 发出的短信
    sms_list_id = (By.ID,"com.android.mms:id/text_view")
    # 要删除的短信
    sms_delete_msg_xpath = (By.XPATH,"//*[contains(@text,'{}')]")
    # 删除
    sms_delete_btn_xpath = (By.XPATH,"//*[contains(@text,'删除')]")
    # 确认删除
    sms_delete_btn_id = (By.ID,"android:id/button1")

