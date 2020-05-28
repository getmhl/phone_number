import os


# 生成完整的手机号
def jxnc(city):
    global roughly, phone_name, dic, x, i
    phone_name = 'phone_' + city + '.txt'
    front_name = 'front_7_ok.txt'

    ok_roughly = open(front_name)
    text = ok_roughly.read()

    roughly = eval(text)

    print(str(len(roughly)) + " = 总号段个数")
    # open(phone_name)
    # os.remove(phone_name)
    dic = open(phone_name, "w")
    for x in range(0, len(roughly)):
        i = 0
        while True:
            i = i + 1
            if i <= 9:
                dic.write(str(roughly[x]) + "000" + str(i))
                dic.write("".join("\n"))
                print(str(roughly[x]) + "000" + str(i))

            elif i <= 99:
                dic.write(str(roughly[x]) + "00" + str(i))
                dic.write("".join("\n"))
                print(str(roughly[x]) + "00" + str(i))

            elif i <= 999:
                dic.write(str(roughly[x]) + "0" + str(i))
                dic.write("".join("\n"))
                print(str(roughly[x]) + "0" + str(i))
            elif i <= 9999:
                dic.write(str(roughly[x]) + str(i))
                dic.write("".join("\n"))
                print(str(roughly[x]) + str(i))

            if i >= 9999:
                break

    dic.close()
    print(city + "地区手机号密码已生成")

# jxnc()

#
# # 前三位电信号段  电脑厉害的可以试试
# # from numpy.core import long
#
# def scdz():
#     global phnum, filwname, dic, x, i
#     phnum = (133, 149, 153, 173, 177, 180, 181, 189, 191, 199
#              )
#     print(len(phnum))
#     filwname = 'jxnc.txt'
#     # os.remove("./phonepassword-11.txt")
#     dic = open(filwname, "a")
#     for x in range(0, len(phnum)):
#         i = 0
#         while True:
#             i = i + 1
#             if i <= 9:
#                 dic.write(str(phnum[x]) + "0000000" + str(i))
#                 dic.write("".join("\n"))
#
#             elif i <= 99:
#                 dic.write(str(phnum[x]) + "000000" + str(i))
#                 dic.write("".join("\n"))
#
#             elif i <= 999:
#                 dic.write(str(phnum[x]) + "00000" + str(i))
#                 dic.write("".join("\n"))
#                 # i + 1
#             elif i <= 9999:
#                 dic.write(str(phnum[x]) + "0000" + str(i))
#                 dic.write("".join("\n"))
#                 # i += 1
#             elif i <= 99999:
#                 dic.write(str(phnum[x]) + "000" + str(i))
#                 dic.write("".join("\n"))
#                 # i += 1
#             elif i <= 999999:
#                 dic.write(str(phnum[x]) + "00" + str(i))
#                 dic.write("".join("\n"))
#                 # i += 1
#             elif i <= 9999999:
#                 dic.write(str(phnum[x]) + "0" + str(i))
#                 dic.write("".join("\n"))
#                 # i += 1
#             elif i <= 99999999:
#                 dic.write(str(phnum[x]) + str(i))
#                 dic.write("".join("\n"))
#                 # i += 1
#
#             if i > 99999999:
#                 break
#
#             print(str(phnum[x]) + str(i))
#     dic.close()
#     print("密码已生成")

# scdz()
