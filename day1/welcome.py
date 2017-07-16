# 登录接口的实现

"""
以字典的方式来记录用户信息，用户信息存储文件的格式为：
zhang:123
li:123
liu:123
最终在程序中变为：
{'zhang ': '123', 'liu ': '123', 'li ': '123'}
便于查找比对。
"""
userinfoFile = open("userinfo.txt", "r") # 打开用户名和密码存储文件
userinfoDict = {}  #创建一个空字典
for line in userinfoFile.readlines():
    (key,value) = line.strip().split(":")  #键值形式存储，用冒号分割。
    userinfoDict[key] = value
userinfoFile.close() # 关闭文件

"""
以列表来记录被锁用户信息，用户信息存储文件的格式为：
li
sugar
最终在程序中变为：
['li', 'sugar']
便于查找比对。
"""
lockinfoFile = open("lockinfo.txt", "r") # 打开锁定用户信息文件
lockinfoList = [ ]
for line in lockinfoFile.readlines():
    lockinfoList.append(line.strip())
lockinfoFile.close() # 关闭文件


print(userinfoDict)
print(lockinfoList)

inputChance = 3 #密码输入错误次数限制
userTmp = "" #临时储存变量，用于核对输入密码错误是否为同一用户
successFlag = 0   # 是否登录成功标识
while successFlag == 0:
    user = input("UserName:")
    pwd = input("Password:")
    for _user in lockinfoList:
        if user == _user:
            print("该用户已经被锁定，请联系管理员处理!")
            successFlag = 1
            break;
    else:
        for _user, _pwd in userinfoDict.items():
            if user == _user and pwd == _pwd:
                print("Welcome {0} to login...".format(user))
                successFlag = 1
                break
            elif user == _user and pwd != _pwd:
                if user != userTmp:
                    inputChance = 3
                inputChance -= 1
                userTmp = user
                if inputChance == 0:
                    print("输入次数超过3次，账户以被锁定")
                    successFlag = 2
                    with open("lockinfo.txt","a") as lk:
                        lk.write("\n")
                        lk.write(user)
                    break
                print("你还剩{0}次机会".format(inputChance))
        else:
            if successFlag == 1:
                break;
            elif successFlag == 2:
                break;
            else:
                print("你输入的用户不存在，请仔细核对")
