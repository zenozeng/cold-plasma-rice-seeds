import pandas
import matplotlib.pyplot as plt

data_23 = pandas.io.excel.read_excel(io='data.xlsx',
                                     sheetname='23',
                                     index_col=0)

data_28 = pandas.io.excel.read_excel(io='data.xlsx',
                                     sheetname='28',
                                     index_col=0)
# print(data_23)
# data_23.plot()
# plt.show()


# 由于初始值存在差异
# 这里统一标准化，以初始点为1
def standardize(arr):
    print(arr)
    base = arr[0]
    arr = list(map(lambda x: x / base, arr))
    print(arr)
    return arr

df = data_28.apply(standardize)

print(df)
df.plot()
plt.show()


# data_28.plot()

# plt.show()
