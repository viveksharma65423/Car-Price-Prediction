Used Car Price Prediction 🚗

Project Overview

This project uses Machine Learning regression models to predict the estimated selling price of used cars based on car age, kilometers driven, fuel type, seller type, transmission, owner type, and car brand.

Objectives

- Analyze and clean used car data.
- Perform Exploratory Data Analysis (EDA).
- Build and compare regression models.
- Predict used car selling prices.
- Develop a web interface using Streamlit.

Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

Machine Learning Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Tuned Random Forest
- Random Forest with Brand Feature

Model Evaluation

The models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The best recorded test R² score in this project was 0.555, achieved by the Random Forest model using the car brand feature.

Features

- Data cleaning and duplicate removal
- Exploratory data analysis and correlation heatmap
- Categorical feature encoding
- Train-test split
- Regression model training and comparison
- Estimated used car price prediction

How to Run the Project

1. Clone or download this repository.

2. Install the required libraries:
   
   pip install -r requirements.txt

3. Run the Streamlit application:
   
   streamlit run app.py

Disclaimer

Predicted prices are estimates and may differ from actual market prices.

Author

Machine Learning Project by Vivek Manoj Sharma
