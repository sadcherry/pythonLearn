# 三级菜单Demo
"""
省市县三级菜单的存储方式
用字典和列表的嵌套来进行设计
{"四川":[{"成都"：["双流县","金堂县","温江"],"广元":["利州区","苍溪县","旺苍县"]}],
"河北":[{"石家庄市"：["长安区","桥西区","灵寿县"],"唐山市":["路南区","古治区","丰南区"]}],
"黑龙江":[{"哈尔滨"：["道里区","道外区","动力区"],"齐齐哈尔":["龙沙区","铁锋区","拜泉县"]}]
}
"""
MENU = {"四川": {"成都":["双流县", "金堂县", "温江"], "广元":["利州区", "苍溪县", "旺苍县"]},
"河北":{"石家庄市":["长安区", "桥西区", "灵寿县"], "唐山市":["路南区", "古治区", "丰南区"]},
"黑龙江":{"哈尔滨":["道里区", "道外区", "动力区"], "齐齐哈尔":["龙沙区", "铁锋区", "拜泉县"]}
}

listTmp = []  #存放当级菜单
level = 1  # 表示所在菜单层级,初始默认处于第一级
while True:
    if level == 1:
        for key in MENU:
            print(key)
            listTmp.append(key)
        province = input("输入你想查看的省：")
        if province in listTmp:
            level = 2
        else:
            level = 1
            print("你输入的省不存在，请重新输入。")
    elif level == 2:
        for key in MENU[province]:
            print(key)
            listTmp.append(key)
        city = input("输入你想查看的市或者输入Y返回上级菜单：")
        if city == "Y":
            level = 1
        elif city in listTmp:
            for key in MENU[province][city]:
                print(key)
                level = 3
                listTmp.append(key)
        else:
            level = 2
            print("你查找的市不存在,请重新输入！")
    elif level == 3:
        country = input("输入Y返回上级菜单：")
        if country == "Y":
            level = 2
        else:
            print("已经是最底层菜单，无法下沉了。")

