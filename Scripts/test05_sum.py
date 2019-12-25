import os

import pytest
import yaml

from Base.getData import GetData


def get_sum_data():
    my_list=[]
    print(os.sep)
    # os.sep: 获取系统路径的分隔符,因为Unix系统分隔符为:"/",Windows系统分隔符为:"\",
    # with open("./data"+os.sep+"sum_data.yaml","r",encoding="utf-8") as f:
    #     data = yaml.safe_load(f)
    data = GetData().get_yml_data("sum.yml")
    print(data)
    for i in data.values():
        my_list.append(tuple(i.values()))
    print(my_list)
    return my_list

class TestSum:

    @pytest.mark.parametrize("a,b,c",get_sum_data())
    def test_sum(self,a,b,c):
        """
        判断两个数之和a+b==c
        :param a:
        :param b:
        :param c:
        :return:
        """
        print("{}+{}={}".format(a,b,c))
        assert a+b==c
