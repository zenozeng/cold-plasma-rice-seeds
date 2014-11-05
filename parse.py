import pandas

data_23 = pandas.io.excel.read_excel(io='data.xlsx',
                                     sheetname='23',
                                     index_col=1)

data_28 = pandas.io.excel.read_excel(io='data.xlsx',
                                     sheetname='28',
                                     index_col=1)
print(data_23)

print(data_28)
