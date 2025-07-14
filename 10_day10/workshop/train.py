import numpy as np
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
import mlflow.sklearn

def load_data():
    df = pd.read_csv("ice_cream.csv")
    X = df[['temp']]
    y = df.iloc[:, -1]
    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=6)
    return X_train, X_test, y_train, y_test

def model_train(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict(model, X_train, X_test):
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    return y_train_pred, y_test_pred

def evaluate(y_test, y_test_pred):
    mae = mean_absolute_error(y_test, y_test_pred)
    mse = mean_squared_error(y_test, y_test_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_test_pred)
    return mae, mse, rmse, r2

def log_model(mae, mse, rmse, r2):
    # Log parameters and metrics
    mlflow.log_param("test_size", 0.5)
    mlflow.log_param("random_state", 6)
    mlflow.log_metric("MAE", mae)
    mlflow.log_metric("MSE", mse)
    mlflow.log_metric("RMSE", rmse)
    mlflow.log_metric("R2", r2)

    eval_results = {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2,
    }

    with open("eval.json", "w") as f:
        json.dump(eval_results, f)

    mlflow.log_artifact("eval.json", artifact_path="eval")
    
def register_model(model):
    # Log the model
    mlflow.sklearn.log_model(registered_model_name="ice cream",
                             sk_model=model,
                             artifact_path="ice_cream")

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = model_train(X_train, y_train)
    y_train_pred, y_test_pred = predict(model, X_train, X_test)
    mae, mse, rmse, r2 = evaluate(y_test, y_test_pred)
    print(f"mae: {mae}, mse: {mse}, rmse : {rmse}, r2: {r2}")
