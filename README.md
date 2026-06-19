# Food Delivery Time Prediction

## Project Overview

This project predicts food delivery times using machine learning.

The goal is to estimate how long a delivery will take based on:

- Delivery person's age
- Delivery person's ratings
- Distance between restaurant and customer
- Type of order
- Type of vehicle

## Tools Used

- Python
- Pandas
- Scikit-Learn
- VS Code

## Data Preparation

- Checked for missing values
- Encoded categorical variables using LabelEncoder
- Created a distance feature from latitude and longitude coordinates

## Model

Linear Regression

## Results

- Mean Absolute Error (MAE): 6.64 minutes
- R² Score: 0.183

## Key Findings

- Vehicle type influences delivery time
- Meal orders tend to take slightly longer
- Distance is more informative than raw coordinates

## Author

Ijegbai Mercy Gift