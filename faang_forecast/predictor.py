import pandas as pd
import numpy as np

import os

from statsmodels.tsa.arima.model import ARIMA

# Class created to predict the closing price of listed stocks
class Predictor:
  # Initialized the predictor by training a model
  # for each ticker and caching the forecast price.
  def __init__(self):
    # This class supports the stocks listed below.
    self.stock_dict = {
      'fb': ['FB.csv', 0],
      'aapl': ['AAPL.csv', 0],
      'amzn' : ['AMZN.csv', 0],
      'nflx' : ['NFLX.csv', 0],
      'goog' : ['GOOG.csv', 0],
      }

    for key in self.stock_dict:
      df = pd.read_csv(self.stock_dict[key][0])
      self.train_and_forecast(key, df)
  # Helper function which will fit the new data to
  # the ARIMA model and cache the forecast result.
  def train_and_forecast(self, ticker_symb, df):
    close_series = df['Close']
      
    history = [x for x in close_series]
      
    model = ARIMA(history, order=(0,1,0))
    model_fit = model.fit()
    output = model_fit.forecast()
    self.stock_dict[ticker_symb][1] = output[0]
  # Called by the client, which will append to the existing
  # stock dataframe.  Here is an example of how the stock_dict
  # will look:
  # dict = {
  #   'Date':['2020-04-02', '2020-04-03',],
  #   'Open':[247.5, 245],
  #   'High':[249, 250],
  #   'Low':[238, 241],
  #   'Close':[241.34, 241.11],
  #   'Adj Close':[241.34, 241.11],
  #   'Volume':[43956200, 43956200],
  # }
  def Update(self, ticker_symb, stock_dict):
    df2 = pd.DataFrame(stock_dict)
    df = pd.read_csv(self.stock_dict[ticker_symb][0])
    df = pd.concat([df, df2], ignore_index = True)
    df.reset_index()
    
    self.train_and_forecast(ticker_symb, df)
    
    df.to_csv(self.stock_dict[ticker_symb][0])
    
  # Return the predicted closing price for the next trading day.
  def Forecast(self, ticker_symb):
    return self.stock_dict[ticker_symb][1]