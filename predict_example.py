from faang_forecast.predictor import Predictor

# Create the predictor instance
p = Predictor()

# Estimate the price for the next day.
print(p.Forecast('aapl'))

# Add two days of stock information to the existing dataset
dict = {
  'Date':['2020-04-02', '2020-04-03',],
  'Open':[247.5, 245],
  'High':[249, 250],
  'Low':[238, 241],
  'Close':[241.34, 241.11],
  'Adj Close':[241.34, 241.11],
  'Volume':[43956200, 43956200],
}
p.Update('aapl', dict)

# Return the updates forecast.
print(p.Forecast('aapl'))