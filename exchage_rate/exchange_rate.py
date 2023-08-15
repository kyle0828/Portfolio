import pandas as pd
from datetime import datetime
import numpy as np


year = str(datetime.now().year)
month = str(datetime.now().month)

month_ls = str(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

if month in month_ls:
    month = '0' + month
else:
    pass

y_m_str = year + "-" + month
currency_ls = ['USD','CNY','HKD','GBP','AUD','CAD','SGD','CHF','JPY','ZAR','SEK','NZD','THB','PHP','IDR','EUR','KRW','VND','MYR']
lst = []
for curr in currency_ls:
    link = 'https://rate.bot.com.tw/xrt/flcsv/0/'+ y_m_str +'/'+ curr
    lst.append(link)

df = pd.DataFrame(lst, columns=['path'])


for i in range(len(df.index)):
    for column in df:
        url = df["path"].values[i]
        rawDf = pd.read_csv(url, index_col=False)
        rawDf['資料日期'] = rawDf['資料日期'].astype(str)

        # Add n blank rows
        n = 29-len(rawDf.index)
        new_df = pd.DataFrame(np.nan, index=range(n), columns=rawDf.columns).reset_index()
    
        res = pd.concat([rawDf, new_df])
        res = res.drop('index', axis=1)
        
        res.to_csv('output_匯率.csv',mode='a', index=False, encoding ='utf_8_sig')