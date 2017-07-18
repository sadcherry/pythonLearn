## 登录接口Demo要求：
  - 输入用户名密码
  - 认证成功后显示欢迎信息
  - 输错三次后锁定

## 相关文件说明
- lockinfo.txt —— 存放被锁用户的信息，只含有用户名
````
以列表来记录被锁用户信息，用户信息存储文件的格式为：
li
sugar
最终在程序中变为：
['li', 'sugar']
便于查找比对。
````
- userinfo.txt ——存放已经注册的用户信息，含有用户名和对应密码
````
以字典的方式来记录用户信息，用户信息存储文件的格式为:
zhang:123
li:123
liu:123
最终在程序中变为：
{'zhang ': '123', 'liu ': '123', 'li ': '123'}
便于查找比对。
````
- welcome.py —— 主程序

## Demo收获
1. 文件的简单读写操作，追加写文件的方式是open("filename","a"),a表示追加。
2. 列表和字典的运用，运用来存储用户相关信息，便于程序的查找比对。
3. for...else...的用法，当for中正常流程完，没有break,则会执行else中的代码。
4. 格式化输出，采用.format()方法的实现。
5. 字符串strip()和split()的用法。
6. 字典的遍历，for _user, _pwd in userinfoDict.items()，items()方法可以直接拆分字典。
7. 学习了画流程图，学会理清思路再动手写代码，希望保持住这个好习惯。大部分的时间应该用在思考上。

## 该Demo流程图

![image](https://github.com/sadcherry/pythonLearn/blob/master/WeclomeDemo/flowchart.png)