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
    plt.figure(figsize=(10,6))
    plt.plot(train_data, label='Training Data')
    plt.plot(test_data, label='Testing Data', color='orange')
    plt.plot(predictions, label='Prediction', color='red')
    plt.title('Stock Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig('results/final_prediction.png')
    plt.close()

    # Calculate Metrics
    report = open('results/report.txt', 'w')
    report.write('Metrics\n')

    rmse = np.sqrt(mean_squared_error(test_data, predictions))
    report.write(f"RMSE: {rmse}")
    report.close()
