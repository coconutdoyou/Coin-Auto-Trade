import pyupbit

access_key = 'xZxEBiAf3OzJasnG1NUO0Ha34jV4o54QGZCYxLx7'
secret_key = 'OkO2tCK795xZA2Flxn3xByQRm20Q8ZMAL5tS3DvK'
upbit = pyupbit.Upbit(access_key, secret_key)

print(upbit.get_balances())
