import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
import train as pipeline

   # Start MLflow tracking]
mlflow.set_tracking_uri("http://192.168.1.36:5001")
mlflow.set_experiment("Experiment_Name")

df = pd.read_csv("ice_cream.csv")
X = df[['temp']]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = pipeline.model_train(X_train, y_train)

y_train_pred, y_test_pred = pipeline.predict(model, X_train, X_test)

mae, mse, rmse, r2 = pipeline.evaluate(y_test, y_test_pred)
pipeline.log_model(mae, mse, rmse, r2)

print('Registering model to pipeline:')
pipeline.register_model(model)