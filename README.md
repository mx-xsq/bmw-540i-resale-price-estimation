# BMW 540i Resale Price Prediction

This project predicts the resale price of BMW 540i vehicles using historical listing data and linear regression.

## Project Files
- `bmw_scrape.py`: Scrapes BMW 540i listings
- `data_cleaning.py`: Cleans and preprocesses raw data
- `EDA.py`: Exploratory data analysis
- `model.py`: Model training and evaluation
- `bmw_540i.csv`: Raw scraped data
- `bmw_540i_cleaned.csv`: Cleaned dataset

## Model Evaluation
The linear regression model achieved:
- MAE: $2,251.92
- RMSE: $2,866.57

A baseline model predicting the average resale price produced an MAE of $4,044.41.  
The trained model reduced prediction error by approximately 45%, demonstrating meaningful predictive value.

## Tools
- Python
- Pandas
- scikit-learn
- NumPy
- Selenium