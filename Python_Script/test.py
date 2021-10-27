'''
Author: your name
Date: 2021-10-27 13:57:41
LastEditTime: 2021-10-27 14:18:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Python_Script\test.py
'''
import pylab as pl
import matplotlib.pyplot as plt
import pandas as pd

# 统计缺失值数量
missing = data.isnull().sum().reset_index().rename(columns={0: 'missNum'})
# 计算缺失比例
missing['missRate'] = missing['missNum']/data.shape[0]
# 按照缺失率排序显示
miss_analy = missing[missing.missRate > 0].sort_values(
    by='missRate', ascending=False)
# miss_analy 存储的是每个变量缺失情况的数据框


fig = plt.figure(figsize=(18, 6))
plt.bar(np.arange(miss_analy.shape[0]), list(
    miss_analy.missRate.values), align='center', color=['red', 'green', 'yellow', 'steelblue'])

plt.title('Histogram of missing value of variables')
plt.xlabel('variables names')
plt.ylabel('missing rate')
# 添加x轴标签，并旋转90度
plt.xticks(np.arange(miss_analy.shape[0]), list(miss_analy['index']))
pl.xticks(rotation=90)
# 添加数值显示
for x, y in enumerate(list(miss_analy.missRate.values)):
    plt.text(x, y+0.12, '{:.2%}'.format(y), ha='center', rotation=90)
plt.ylim([0, 1.2])

plt.show()
