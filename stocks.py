import quandl
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Get the data
df = quandl.get("WIKI/AMZN")
#Look at the data
print(df.head())

#Get the Adjusted Close Price
df = df[['Adj. Close']]
#Look at the new data
print(df.head())

#Number of days to forecast
forecastDays = 30

#Create another column (the target) shifter 'forecastDays' units up
df['Prediction'] = df[['Adj. Close']].shift(-forecastDays)
#print new data set
print(df.tail())

#Create the independent seta set (X)
#Conver the dataframe to a numpy array
X = np.array(df.drop(['Prediction'],1))
#Remove the last 'forecasrDays'
X = X[:-forecastDays]
print(X)

#Create the dependent data set (y)
#Convert the dataframe to a numpy array (All of the values including the NaN)
y = np.array(df['Prediction'])
#Get all the target values (y) except the forecastDays
y = y[:-forecastDays]
print(y)

#Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#Create and train the Support Vector Machine (Regressor)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

#Testing Model: Score return the coefficient of determination R^2 of the prediction
#The best posssible score = 1
svm_confidence = svr_rbf.score(x_test, y_test)
print("svm confidence: ", svm_confidence)

#Create and train the Linear Regression Model 
lr = LinearRegression()
#Train the model
lr.fit(x_train, y_train)

#Testing Model: Score return the coefficient of determination R^2 of the prediction
#The best posssible score = 1
lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# Set x_forecast equal to the last 30 rows of the orginal data set from Adj. Close
x_forecast = np.array(df.drop(['Prediction'],1))[-forecastDays:]
print(x_forecast)

#Print the linear regression predictions for the 'n' days 
lr_prediction = lr.predict(x_forecast)
print(lr_prediction)

#Print the svm predictions for the 'n' days 
svr_prediction = svr_rbf.predict(x_forecast)
print(svr_prediction)
