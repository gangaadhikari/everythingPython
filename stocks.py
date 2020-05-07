import quandl
import numpy
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Get the data
df = quandl.get("WIKI/TSLA")
#Look at the data
print(df.head())

#Get the Adjusted Close Price
df = df[['Adj. Close']]
#Look at the new data
print(df.head())

#Number of days to forecast
forecastDays = 1

#Create another column (the target) shifter 'n' units up
df['Prediction'] = df[['Adj.Close']].shift(-1)
#print new data set
print(df.head())
