# 简单Shell Sed替换功能实现

## 文件说明

- a.txt —— 要替换的文件
- b.txt —— 替换后重新生成的新文件
- shellsed.py —— 主程序文件

## Demo 收获

1. 文件的操作，可以在with语句中打开多个文件,with open(sedFile,"r") as f, open("b.txt","w+") as f2:
2. f2.flush() 保证写刷新到硬盘中
3. 循环读文件中的每一行，可以使用 for line in f: 这种格式
4. 要从命令行读取参数，可以引入sys模块，sys.argv即是参数组。