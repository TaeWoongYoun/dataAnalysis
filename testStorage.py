import pandas as pd
import yfinance as yf

df_tsla = yf.download('TSLA', start='2021-11-01', end='2023-03-31')
df_tsla.to_excel("./TSLA_OHLCV1.xlsx")