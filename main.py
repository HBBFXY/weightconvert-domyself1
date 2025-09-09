import math   #运用math第三方包解决四舍五入问题
WeightStr = input("请输入带单位的重量值: ").strip()
if WeightStr[-2:] == "kg": 
    value = float(WeightStr[0:-2])
    pd = value * 2.2046
    pd = math.floor(pd * 1000) / 1000  # 保留三位小数，向下取整
    print("对应的英制重量为{:.3f}磅".format(pd))
elif WeightStr[-2:] == "pd":
    value = float(WeightStr[0:-2])
    kg = value / 2.2046
    kg = math.floor(kg * 1000) / 1000  # 保留三位小数，向下取整
    print("对应的公制重量为{:.3f}公斤".format(kg))
else:
    print("输入格式错误，请输入类似 '10kg' 或 '10pd'")
