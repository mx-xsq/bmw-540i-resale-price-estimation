import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("bmw_540i_cleaned.csv")

# Preview data
print("First 5 rows:")
print(df.head())

# Structure info
print("\nDataFrame info:")
df.info()

# Statistical summary
print("\nStatistical summary:")
print(df.describe())

# Scatter plot: price vs mileage
plt.figure()
plt.scatter(df["Mileage"], df["Price"])
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Price vs Mileage")
plt.show()

# Average price by car's age
print("\nAverage price by car age:")
print(df.groupby("car_age")["Price"].mean())

# Average price by Trim
print("\nAverage price by Trim:")
print(df.groupby("Trim")["Price"].mean())
