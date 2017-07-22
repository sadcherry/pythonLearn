# 购物车程序（用户版）

"""
-用户入口
  - 商品信息存在文件里
  - 已购商品，余额记录
- 商家入口
  - 可以添加商品，修改商品价格
"""

# 打开用户文件
with open("user.txt", "r") as f:
    userinfo = f.read()
    if len(userinfo) == 0:         # 如果文件为空，则新建字典为空
        userinfo = {}
    else:
        userinfo = eval(userinfo)   # 将字符串转换为字典

# 打开商品文件
with open("goods.txt","r") as f:
    goodsinfo = f.read()
    if len(goodsinfo) == 0:          # 如果文件为空，则新建字典为空
        goodsinfo = {}
    else:
        goodsinfo = eval(goodsinfo)   # 将字符串转换为字典

user = input("输入你的登录名>>>")

if user in userinfo:
    print("你之前已购买过商品")
    print("你购买的商品为：")
    for i in userinfo[user][0]:
        print(i)
    salary = userinfo[user][1]
    print("你的余额为{0}".format(salary))
else:
    while True:
        salary = input("输入你的银行存款:")
        try:
            if salary.isdigit:
                salary = int(salary)
                userinfo[user] = [[],0]
                break
        except:
            print("你输入的工资有误，请重新输入")

while True:
    print("-------可以购买的商品及商品价格如下---------")
    for i in goodsinfo:         # 打印已有商品
        print(i, goodsinfo[i])
    goodschoice = input("输入你要购买的商品（退出购买按q）>>>")
    if goodschoice == "q":              # 退出程序
        print("-------你最终购买的商品为----------")
        for i in userinfo[user][0]:
            print(i)
        with open("user.txt","w") as f:
            str = str(userinfo)       # 字典转换为字符串，才可以写入文件
            f.write(str)
        print("你的最终余额为 {0}".format(userinfo[user][1]))
        break
    elif goodschoice in goodsinfo:
        if salary >= goodsinfo[goodschoice]:
            print("商品已加入购物车")
            userinfo[user][0].append(goodschoice)
            salary -= goodsinfo[goodschoice]
            userinfo[user][1] = salary
            print("你购买的当前商品为{0},当前余额为{1}".format(goodschoice, salary))
        else:
            print("钱不够，快去赚钱吧！！！")
    else:
        print("你输入的商品不存在，请重新输入！")
