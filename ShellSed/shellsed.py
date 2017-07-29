# -*- coding:UTF-8 -*-
import sys

sedOld = sys.argv[1]   # 原字符串
sedNew = sys.argv[2]   # 要替换的字符串
sedFile = sys.argv[3]  # 查找字符串的文件

print(sedOld,sedNew,sedFile)

# 通过打开两个文件来进行操作，一个只读，一个进行写。
with open(sedFile,"r") as f, open("b.txt","w+") as f2:
    for line in f:
        if sedOld in line:
            line = line.replace(sedOld,sedNew)
        f2.write(line)
        f2.flush()     # 刷新文件到硬盘中
