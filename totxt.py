# -*- codeing = utf-8 -*-
# @Time : 2021/11/26 11:22
# @Author : 王大洋
# @Flie : totxt.py
# @Software : PyCharm
import pandas as pd

df = pd.read_excel('1.xlsx', sheet_name='教育', header=None)		# 使用pandas模块读取数据
print('开始写入txt文件...')
df.to_csv('txt/all.txt', header=None, sep=',', index=False)		# 写入，逗号分隔
print('文件写入成功!')

