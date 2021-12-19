import pyupbit
import math
import time

access_key = 'xZxEBiAf3OzJasnG1NUO0Ha34jV4o54QGZCYxLx7'
secret_key = 'OkO2tCK795xZA2Flxn3xByQRm20Q8ZMAL5tS3DvK'
upbit = pyupbit.Upbit(access_key, secret_key)

# 차트에서 최근 count 개의 평균값을 반환
def get_average(coin, count, interval) :		
    df = pyupbit.get_ohlcv(coin, count = count, interval = interval)
    avg = sum(df.close) / count
    return avg

# 시장가로 모두 매도
def sell_market_all(coin) :
    balance = upbit.get_balance(coin)
    if balance > 0 :
        upbit.sell_market_order(coin, balance)

# 시장가로 모두 매수
def buy_market_all(coin) :
    balance = math.floor(upbit.get_balance("KRW")) - 50
    if balance >= 5000 :
        upbit.buy_market_order(coin, balance)


if __name__ == '__main__': 
    try:
        coin = "KRW-BTC"
        count = 5
        interval = "minute15"

        while True :
            cur_price = pyupbit.get_current_price(coin)			# 현재가
            dest_price = get_average(coin, count, interval)		# 목표가
            
            # 현재가가 목표가보다 낮아지면 매도
            if cur_price < dest_price :
            	sell_market_all(coin)
            	time.sleep(1)
            
            # 현재가가 목표가보다 높아지면 매수
            else :
            	buy_market_all(coin)
            	time.sleep(1)
            time.sleep(1)

    except Exception as ex:
        sys.exit(0)