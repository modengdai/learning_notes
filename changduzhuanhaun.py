#长度转换,1 米 = 39.37 英寸
l=input()
if l[-1]in ['m']:
  inch=eval(l[0:-1])*39.37
  print("{:.3f}in".format(inch))
elif l[-2:]in ["in"]:
  m=eval(l[0:-2])/39.37
  print("{:.3f}m".format(m))
else:
  print("输入错误！")
