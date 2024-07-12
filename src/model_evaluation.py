# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import joblib

def evaluate_model(model_fit, training_data, testing_data):

    train_data = pd.read_csv(training_data)
    test_data = pd.read_csv(testing_data)

    train_data = train_data['Close/Last']
    test_data = test_data['Close/Last']

    predictions = model_fit.predict(start=len(train_data), end=len(train_data) + len(test_data) - 1, typ='levels')

    # Plot the prediction
    fig8, ax8 = plt.subplots(figsize=(10,6))
    ax8.plot(train_data, label='Training Data')
    ax8.plot(test_data, label='Testing Data', color='orange')
    ax8.plot(predictions, label='Prediction', color='red')
    ax8.set_title('Stock Price Prediction')
    ax8.set_xlabel('Date')
    ax8.set_ylabel('Price')
    ax8.legend()

    # Calculate Metrics
    rmse = np.sqrt(mean_squared_error(test_data, predictions))

    return fig8, rmse