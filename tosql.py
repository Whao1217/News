# -*- coding: utf-8 -*-

# 导入必要模块
import pandas as pd
from sqlalchemy import create_engine
import pymysql

# 初始化数据库连接，使用pymysql模块
db_info = {'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': 3306,
            'database': 'news'
            }

engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info, encoding='utf-8')
# 直接使用下一种形式也可以
# engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')

# 读取本地CSV文件
#df = pd.read_csv("1.xlsx", sep='/t')
df = pd.read_excel("1.xlsx",sheet_name="娱乐")
print(df)
# 将新建的DataFrame储存为MySQL中的数据表，不储存index列(index=False)
# if_exists:
# 1.fail:如果表存在，啥也不做
# 2.replace:如果表存在，删了表，再建立一个新表，把数据插入
# 3.append:如果表存在，把数据插入，如果表不存在创建一个表！！
pd.io.sql.to_sql(df, 'yule', con=engine, index=False, if_exists='replace')
# df.to_sql('example', con=engine,  if_exists='replace')这种形式也可以
print("Write to MySQL successfully!")

