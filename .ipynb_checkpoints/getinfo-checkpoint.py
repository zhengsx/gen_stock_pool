import tushare as ts

info = ts.get_industry_classified()
info.to_excel('info.xlsx')
