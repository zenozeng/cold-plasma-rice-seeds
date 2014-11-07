#!/usr/bin/python3

import pandas
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

df_23.plot(kind='bar', stacked=True, alpha=1)
df_28.plot(kind='bar', stacked=True, alpha=1)
plt.show()
# df_28.plot(ax=ax)

# plt.figure()
# df_23.plot()

# plt.figure()
# df_28.plot()

# plt.show()
