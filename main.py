Weight = input("请输入带单位的重量值: ")
if Weight[-2:] == "kg":  
    pd = eval(Weight[0:-2]) * 2.2046
    print("对应的英制重量为{:.3f}磅".format(pd))
elif Weight[-2:] == "pd":
    kg = eval(Weight[0:-2]) / 2.2046
    print("对应的公制重量为{:.3f}公斤".format(kg))
else:
    print("输入格式错误，请输入类似 '10kg' 或 '10pd'")
