import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


df = pd.read_csv("bmw_540i_cleaned.csv")

# Prepare the Data
X = df[["Mileage", "car_age", "Trim"]]
y = df["Price"]

# Split the Data (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# -----------------------------------------------------------------------------
# Model Evaluation
# -----------------------------------------------------------------------------

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"MAE: ${mae:,.2f}")
print(f"RMSE: ${rmse:,.2f}")

# Baseline model: predict the mean price
baseline_price = y_train.mean()
y_pred_baseline = [baseline_price] * len(y_test)

baseline_mae = mean_absolute_error(y_test, y_pred_baseline)

print(f"Baseline MAE: ${baseline_mae:,.2f}")
