import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([1, 2, 3])

model = LinearRegression()
model.fit(X, y)

predicted = model.predict(X)
print(model.predict([[7, 8]]))
