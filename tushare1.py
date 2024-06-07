import tushare as ts
from datetime import datetime, timedelta
import pandas as pd

change = []
def tu(gupiao):
    # 设置Tushare token
    token = 'd958bcbbacf596c58dd50f46c524149fea7714747222f8192fe14fad'
    ts.set_token(token)
    pro = ts.pro_api()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=100)
    for code in gupiao:
        if code[0]=='6':
            df = pro.daily(ts_code= code+'.SH', start_date=start_date.strftime('%Y%m%d'), end_date=end_date.strftime('%Y%m%d'))
        else:
            df = pro.daily(ts_code= code+'.SZ', start_date=start_date.strftime('%Y%m%d'), end_date=end_date.strftime('%Y%m%d'))
        df.rename(columns={'trade_date': 'date'}, inplace=True)
        change.append(df.iloc[0,7])
        # print(df)
        # # 反转DataFrame
        df = df.iloc[::-1].reset_index(drop=True)
        # print(df)

        df['date'] = pd.to_datetime(df['date'])
        df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        df.to_csv("./data3/"+ code +'.csv')
        df = df[['ts_code', 'date','close',  'vol', 'amount','open', 'high', 'low']]
        # df.columns = ['Stkcd', 'Trddt', 'Opnprc', 'Hiprc', 'Loprc', 'Clsprc','Dnshrtrd', 'Dnvaltrd']
        df.rename(columns={'ts_code':'Stkcd','date':'Trddt','close':'Clsprc','vol':'Dnshrtrd','open':'Opnprc','high':'Hiprc','low':'Loprc','amount':'Dnvaltrd'}, inplace=True)
        df.to_csv("./data4/" + code + '.csv',index=False)
    return change


if __name__ == "__main__":
    gupiao = ['000737', '600016', '600036', '601919','000767','002594','300001','605499','000777','000788']
    print(tu(gupiao))

