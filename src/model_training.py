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
    fig7, ax7 =plt.subplots(figsize=(10,6))
    ax7.plot(training_data.index, training_data, label='Historical Data')
    ax7.plot(forecast.index , forecast, label='Forecast', color='red')
    ax7.set_xlabel('Date')
    ax7.set_ylabel('Close Price')
    ax7.set_title('Stock Price Forecast')
    ax7.legend()

    # returning the trained model and the forecast plot
    return fig7, model_fitted