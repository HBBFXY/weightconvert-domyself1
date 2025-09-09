# WeightConvert.py
WeightStr = input("请输入带单位的重量值: ")

if WeightStr[-2:] == "kg":   # 如果输入以 "kg" 结尾
    pd = eval(WeightStr[0:-2]) * 2.2046
    print("对应的英制重量为{:.3f}磅".format(pd))

elif WeightStr[-2:] == "pd": # 如果输入以 "pd" 结尾
    kg = eval(WeightStr[0:-2]) / 2.2046
    print("对应的公制重量为{:.3f}公斤".format(kg))

else:
    print("输入格式错误，请输入类似 '10kg' 或 '10pd'")写代码，题目具体要求见README.md文件
