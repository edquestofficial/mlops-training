    
# from fastapi import FastAPI
# from pydantic import BaseModel
# import pickle
# import numpy as np

# # Load the saved model
# with open("linear_regression_model.pkl", "rb") as f:
#     model = pickle.load(f)

# app = FastAPI()

# class InputData(BaseModel):
#     temp: float

# @app.get("/")
# def read_root():
#     return {"message": "Ice Cream Sales Predictor is running!"}

# @app.post("/predict")
# def predict_sales(data: InputData):
#     input_array = np.array([[data.temp]])
#     prediction = model.predict(input_array)
#     return {"predicted_sales": prediction[0]}


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pickle
import numpy as np

# Load the saved model
with open("linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Updated to accept a list of temps
class InputData(BaseModel):
    temps: List[float]

@app.get("/")
def read_root():
    return {"message": "Ice Cream Sales Predictor is running!"}

@app.post("/predict")
def predict_sales(data: InputData):
    input_array = np.array(data.temps).reshape(-1, 1)
    prediction = model.predict(input_array)
    return {"predicted_sales": prediction.tolist()}
