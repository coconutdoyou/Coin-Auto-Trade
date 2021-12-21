import pyupbit
import pandas as pd
import numpy as np
import time

# rr = Rate Of Return
# crr = Cumulative Rate Of Return
# mdd = Max Draw Down, dd = Draw Down

def get_data(data_count)
    for i in range(data_count // 200 + 1): #upbit 에서 한번에 200개씩 밖에 데이터를 안 줌
        if i < data_count // 200 :
            df = pyupbit.get_ohlcv(coin, to = date, interval = interval)
            date = df.index[0]
        elif data_count % 200 != 0 : #data_count가 200의 배수가 아닐 때 찌끄레기 처리
            df = pyupbit.get_ohlcv(coin, to = date, interval = interval, count = data_count % 200)
        else :
            break

        dfs.append(df) 
        time.sleep(0.1)

coin = "KRW-BTC"
interval = "day"
fees = 0.0005
data_count = 1500

date = None
dfs = [ ]

