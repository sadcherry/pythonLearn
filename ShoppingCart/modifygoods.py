# 管理员修改商品信息，增加或删除商品、修改价格等。

"""
-用户入口
  - 商品信息存在文件里
  - 已购商品，余额记录
- 商家入口
  - 可以添加商品，修改商品价格等
"""

with open("goods.txt", "r") as f:
    reads = f.read()
    if len(reads) == 0:
        print("商品不存在，请添加商品信息！")
    else:
        goods = eval(reads)
        print("已存在商品的信息为:")
        for i in goods:
            print(i, goods[i])

while True:
    choice = input("输入你想选择的操作：\n"
          "1.增加商品  2.删除商品  3.修改价格 4.退出操作\n"
          ">>>")
    if choice in ["1", "2", "3","4"]:
        if choice == "1":
            g = input("输入要增加的商品名称>>>")
            v = input("输入要增加的商品价格>>>")
            goods[g] = int(v)
            print("增加成功....")
        elif choice == "2":
            g = input("输入你想删除的商品的名称>>>")
            if g in goods:
                del goods[g]
                print("删除陈功...")
            else:
                print("你想删除的商品不存在.")
        elif choice == "3":
            g = input("输入你想修改价格的商品的名称>>>")
            if g in goods:
                v = input("输入你想修改的价格>>>")
                goods[g] = int(v)
            else:
                print("你想删除的商品不存在.")
        else:
            str = str(goods)
            with open("goods.txt","w") as f:
                f.write(str)
            print("成功退出....")
            break