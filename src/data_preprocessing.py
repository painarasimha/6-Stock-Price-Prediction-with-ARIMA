# Import Libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
import joblib
import os

def load_data(filepath):
    data = pd.read_csv(filepath)
    print(data.head(5))

    # Preprocess
    print(f"Number of Rows: {data.shape[0]}")
    print(f"Number of Columns: {data.shape[1]}")

    print(f"{data.info()}")  # No Null Values.

    print(data['Company'].value_counts()) # Therefore we have 10 companies, with each company having 2516 data points.
    
    # Train Test Split
    tscv = TimeSeriesSplit(n_splits=5)
    data_splits = tscv.split(data)

    train_data = pd.DataFrame()
    test_data = pd.DataFrame()

    for i, (train_index, test_index) in enumerate(data_splits):
        train_set = data.iloc[train_index]
        test_set = data.iloc[test_index]

        train_data = pd.concat([train_data, train_set])
        test_data = pd.concat([test_data, test_set])

    # Checking for the shape of training and testing set

    print(f"Training Data : {train_data.shape}")
    print(f"Testing Data : {test_data.shape}")

    # Saving the training and testing dataset

    train_data.to_csv('data/training_data.csv', index=False)
    test_data.to_csv('data/testing_data.csv', index=False)