from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# 🎯 Your Dataset
data = {
    "size": [2000, 1600, 1500, 1800, 1900, 1400, 1400, 1500, 1550, 1600],
    "bedrooms": [3, 2, 2, 3, 3, 2, 2, 2, 2, 3],
    "price": [500000, 450000, 400000, 480000, 520000, 420000, 410000, 440000, 430000, 460000]
}

df = pd.DataFrame(data)

# 🎯 Input & Output
X = df[["size", "bedrooms"]]
y = df["price"]

# 🎯 Train-Test Split
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# 🎯 Building AI Model
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(2,)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)
])

# 🎯 Compiling Model
model.compile(optimizer="adam", loss="mean_squared_error")

# 🎯 Training the Model
model.fit(X_train, y_train, epochs=100, verbose=0)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return "Prediction Route Working!"

if __name__ == '__main__':
    app.run(debug=True)
