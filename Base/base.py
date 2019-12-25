from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver

    def search_ele(self,loc,timeout=5,poll=1):
        """
        定位一个元素
        :param loc:元组
        :param timeout:搜索元素超时时长
        :param poll:搜索元素时间间隔
        :return:元素对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self,loc,timeout=5,poll=1):
        """
        定位一组元素
        :param loc:元组
        :param timeout:搜索元素超时时长
        :param poll:搜索元素时间间隔
        :return:一组元素对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self,loc,timeout=5,poll=1):
        """
        元素点击
        :param loc:元组
        :param timeout:搜索元素超时时长
        :param poll:搜索元素时间间隔
        :return:
        """
        self.search_ele(loc,timeout,poll).click()

    def send_ele(self,loc,text,timeout=5,poll=1):
        """
        元素输入
        :param loc:元组
        :param timeout:搜索元素超时时长
        :param poll:搜索元素时间间隔
        :return:
        """
        ele = self.search_ele(loc,timeout,poll)
        ele.clear()
        ele.send_keys(text)
