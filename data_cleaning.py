import pandas as pd
import re
from datetime import datetime

# ---------------------------------------------------------
# functions definition
# ---------------------------------------------------------

def clean_trim(text):
    """
    Convert trim to numeric:
    RWD -> 0
    AWD -> 1
    Everything else -> None
    """

    if text == "RWD":
        return 0
    if text == "AWD":
        return 1
    else:
        return None
    
def clean_number(text):
    return int("".join(re.findall(r"\d+", text)))

# -----------------------------
# 1. Load raw scraped data
# -----------------------------
df = pd.read_csv("bmw_540i.csv")

print("Initial shape:", df.shape)
print(df.head())

# ------ clean trim ------

df["Trim"] = df["Trim"].apply(clean_trim)
df = df.dropna(subset=["Trim"])
df["Trim"] = df["Trim"].astype(int)

# ------ clean price and mileage ------

df["Price"] = df["Price"].apply(clean_number)
df["Mileage"] = df["Mileage"].apply(clean_number)

# ------ clean year ------

df["Year"] = df["Year"].astype(int)

# ------ add new column: car_age ------

CURRENT_YEAR = datetime.now().year
df["car_age"] = CURRENT_YEAR - df["Year"]

# -----------------------------
# 9. Final check
# -----------------------------
print("Cleaned shape:", df.shape)
print(df.describe())


# -----------------------------
# 10. Save cleaned dataset
# -----------------------------
df.to_csv("bmw_540i_cleaned.csv", index=False)

print("Cleaning complete. Saved to bmw_540i_cleaned.csv")