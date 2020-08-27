import tushare as ts
import pandas as pd
from pyecharts.charts import Kline
from pyecharts import options as opts
#正常显示画图时出现的中文和负号

ts.set_token('c80d06f9656ddb0850d8dc2de18a2db266652d4b456bab187673248e')
pro=ts.pro_api()

#获取当前上市的股票代码、简称、注册地、行业、上市时间等数据
basic=pro.stock_basic(list_status='L')
#查看前五行数据
#basic.head(5)

#获取平安银行日行情数据
pa=pro.daily(ts_code='000001.SZ', start_date='20190101',
               end_date='20190106')
#pa.head()

#K线图可视化

pa.index=pd.to_datetime(pa.trade_date)
pa=pa.sort_index()
print(pa)
v1=list(pa.loc[:,['open','close','low','high']].values.tolist())
t=pa.index
v0=list(t.strftime('%Y%m%d'))

print(v0)
print(v1)
kline = (
    Kline()
    .add_xaxis(v0)
    .add_yaxis("kline", v1)
    .set_global_opts(title_opts=opts.TitleOpts(title="平安银行K线图"))
)
kline.render("3.html")