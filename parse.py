#!/usr/bin/python3

import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt

from mpltools import style
style.use('ggplot')

data_23 = pandas.io.excel.read_excel(io='data.xlsx',
                                     sheetname='23',
                                     index_col=0)

data_28 = pandas.io.excel.read_excel(io='data.xlsx',
                                     sheetname='28',
                                     index_col=0)


# 由于初始值存在差异
# 这里统一标准化，以初始质量为1，计算各个时间段的增长率
def standardize(arr):
    base = arr[0]
    arr = list(map(lambda x: x / base, arr))
    for i in reversed(range(1, len(arr))) :
        arr[i] -= arr[i-1]
    arr[0] = 0
    return arr

df_23 = data_23.apply(standardize).transpose()
df_28 = data_28.apply(standardize).transpose()

print(df_23)

fig, axes = plt.subplots(nrows=1, ncols=2)

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Source Han Sans CN'
mpl.rcParams['axes.titlesize'] = 'large'

df_23.plot(ax=axes[0],
           kind='area',
           stacked=True,
           alpha=0.5,
           ylim=[0, 0.3],
           linewidth=1.0,
           title='（陈）浙优023')

df_28.plot(ax=axes[1],
           kind='area',
           stacked=True,
           alpha=0.5,
           ylim=[0, 0.3],
           linewidth=1.0,
           title='津粳优028')

plt.show()
