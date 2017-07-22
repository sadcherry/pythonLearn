# 购物车Demo

## Demo要求
- 用户版本
  - 商品信息存在文件里
  - 已购商品，余额记录
- 商家版本
  - 可以添加商品，修改商品价格等

 ## 文件说明

  - goods.txt       ——存放商品信息
    - 商品以字典的形式储存，名称和价格，如{'Ipone': 3500, 'Coffee': 30, 'Mac': 9888}
  - user.txt        ——存放用户购买信息
    - 用户购买信息是一个字典和列表的嵌套，包含用户名称，购买商品，剩余金额。如{'sugar': [['Car', 'Mac'], 890112]}
  - ShoppingCart.py ——用户版本的购物车
  - modifygoods.py  ——商家版修改商品文件
  - flowchart.png    ——程序设计流程图

  ## Demo 收获

  1. 判断文件是否为空，可以通过检测长度是否为0来判断。if len(所读内容)
  2. 字符串与字典的转换,这是为了能让写入文件或将文件中的字典格式的字符串转换成字典。
      - 字符串转字典 dict = eval(str)
      - 字典转字符串 str = str(dict)
  3. 字典的常见操作，增删改查。

## 流程图（购物车用户版）

![image](https://github.com/sadcherry/pythonLearn/blob/master/ShoppingCart/flowchart.png)