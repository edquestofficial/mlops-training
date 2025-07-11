
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def load_data():
    df = pd.read_csv("ice_cream.csv")
    return df

def split_features_labels(df):
    X = df[['temp']]
    Y = df.iloc[:, -1]
    return X, Y

def split_data(X, Y, test_size=0.2, random_state=1):
    return train_test_split(X, Y, test_size=test_size, random_state=random_state)

def initialize_model():
    return LinearRegression()

def train_model(model, X_train, Y_train):
    model.fit(X_train, Y_train)
    return model

def save_model_pickle(model, filename='linear_regression_model.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

def load_model_pickle(filename='linear_regression_model.pkl'):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def predict(model, X):
    return model.predict(X)

def evaluate_model(Y_true, Y_pred):
    mae = mean_absolute_error(Y_true, Y_pred)
    mse = mean_squared_error(Y_true, Y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(Y_true, Y_pred)

    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"R² Score: {r2:.2f}")

def main():
    df = load_data()
    X, Y = split_features_labels(df)
    X_train, X_test, Y_train, Y_test = split_data(X, Y)

    model = initialize_model()
    model = train_model(model, X_train, Y_train)

    save_model_pickle(model)
    loaded_model = load_model_pickle()

    Y_train_pred = predict(loaded_model, X_train)
    Y_test_pred = predict(loaded_model, X_test)

    evaluate_model(Y_test, Y_test_pred)

if __name__ == '__main__':
    main()
