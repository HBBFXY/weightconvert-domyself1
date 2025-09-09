Weight = input("请输入带单位的重量值: ")
if Weight[-2:] == "kg":   # 输入以 kg 结尾
    value = float(Weight[0:-2])
    pd = value * 2.2046
    pd = int(pd * 1000) / 1000   # 截断保留三位小数
    print("对应的英制重量为{:.3f}磅".format(pd))
elif Weight[-2:] == "pd": # 输入以 pd 结尾
    value = float(Weight[0:-2])
    kg = value / 2.2046
    kg = int(kg * 1000) / 1000   # 截断保留三位小数
    print("对应的公制重量为{:.3f}公斤".format(kg))
else:
    print("输入格式错误，请输入类似 '10kg' 或 '10pd'")
