# -*- coding: UTF-8 -*-

import jieba
import collections
import re
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts import options as opts
from pyecharts.globals import ThemeType, CurrentConfig

CurrentConfig.ONLINE_HOST = 'http://127.0.0.1:5000/ciyuntu'

# 958条评论数据
with open('txt/youxi.txt','r', encoding='UTF-8') as f:
    data = f.read()

# 文本预处理  去除一些无用的字符   只提取出中文出来
new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)  # 只要字符串中的中文
new_data = " ".join(new_data)

# 文本分词--精确模式分词
seg_list_exact = jieba.cut(new_data, cut_all=True)

result_list = []
with open('stopword/stopword.txt', encoding='utf-8') as f:
    con = f.readlines()
    stop_words = set()
    for i in con:
        i = i.replace("\n", "")  # 去掉读取每一行数据的\n
        stop_words.add(i)

for word in seg_list_exact:
    # 设置停用词并去除单个词
    if word not in stop_words and len(word) > 1:
        result_list.append(word)
print(result_list)

# 筛选后统计
word_counts = collections.Counter(result_list)
# 获取前100最高频的词
word_counts_top100 = word_counts.most_common(30)
# 可以打印出来看看统计的词频
print(word_counts_top100)

word1 = WordCloud(init_opts=opts.InitOpts(width='1350px', height='750px', theme=ThemeType.MACARONS))
word1.add('词频', data_pair=word_counts_top100,
          word_size_range=[15, 108], textstyle_opts=opts.TextStyleOpts(font_family='cursive'),
          shape=SymbolType.DIAMOND)
word1.set_global_opts(title_opts=opts.TitleOpts('词云图'),
                      toolbox_opts=opts.ToolboxOpts(is_show=True, orient='vertical'),
                      tooltip_opts=opts.TooltipOpts(is_show=True, background_color='red', border_color='yellow'))
word1.render("ciyuntu1.html")

