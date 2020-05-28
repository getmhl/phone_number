import os
import number.A
# 处理前7位手机号,将其末尾加上逗号，
filename = "front_7.txt"
write_name = 'front_7_ok.txt'
input("切勿将软件用于非法用途，确保已替换front.txt内容后回车继续")
city = input("请输入号段所属区号：")
while not city:
    city = input("请输入号段所属区号：")

os.remove(write_name)
hao = open(filename, "r")
ma = open(write_name, "a")
text1 = hao.read()
print(str(len(text1)) + ' = 号段文件总字符数')

hao.close()
hao1 = open(filename, "r")
for i in range(0, int(len(text1)/7)):
    text = hao1.read(7)
    ma.write(text+", ")
    # 添加逗号
    # print(text+", ")，
hao1.close()
ma.close()
number.A.jxnc(city)
