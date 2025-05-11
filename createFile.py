import pandas as pd
import yfinance as yf
import datetime as dt

df_tsla = yf.download('TSLA', start='2021-11-01', end=dt.date.today())
df_tsla.to_csv("./TSLA_OHLCV.csv")