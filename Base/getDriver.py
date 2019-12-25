from appium import webdriver


def get_android_driver(pac,act):
    """
    返回Android 手机驱动对象
    :param pac: 包名
    :param act: 启动名
    :return:
    """
    capabilities = {
        "platformName": "Android", # 测试的平台(Android和iOS)
        "platformVersion": "5.1", # 设备系统版本
        "deviceName": "模拟器", # 设备名称
        "appPackage": pac, # 待测应用包名
        "appActivity": act, # 待测应用的启动名
        'resetKeyboard': True, # 解决脚本输入中文的问题
        'unicodeKeyboard': True
    }
    # com.android.settings/.Settings
    # 返回驱动对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=capabilities)
