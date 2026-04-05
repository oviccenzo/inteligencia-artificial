import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.callbacks import EarlyStopping

ticketr = "tsla"
star_date = "2015-01-01"
end_date = None
df = yf.download(ticketr, start=star_date, end=end_date)
print()
print(df.head())
print(df.tail())