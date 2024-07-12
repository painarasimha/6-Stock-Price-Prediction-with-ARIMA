# Importing Libraries

import pandas as pd
import joblib
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def train_model(data, order=(5,1,0)):
    # Load training data
    train = pd.read_csv(data)
    try:
        train['Date'] = pd.to_datetime(train['Date'], format='%m-%d-%Y', dayfirst=True)
    except ValueError:
        train['Date'] = pd.to_datetime(train['Date'], format='%m/%d/%Y', dayfirst=False)
    

    train = train.sort_values(by='Date')

    train.set_index('Date', inplace=True)

    training_data = train['Close/Last']

    model = ARIMA(training_data, order=order)
    model_fitted = model.fit()

    print(model_fitted.summary())

    # Plot the forecast
    forecast = model_fitted.forecast(steps=30)
    plt.figure(figsize=(10,6))
    plt.plot(training_data.index, training_data, label='Historical Data')
    plt.plot(forecast.index , forecast, label='Forecast', color='red')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Price Forecast')
    plt.legend()
    plt.savefig('results/forecast.png')
    plt.close()


    # Saving the trained model using joblib
    joblib.dump(model_fitted, 'models/ARIMA_model.pkl')

if __name__ == '__main__':
    train_model('data/training_data.csv')