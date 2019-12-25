import yaml

# 读取文件
with open("./value2.yaml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)

    # 打印数据
    print(data)
    # print(type(data["value24"]))