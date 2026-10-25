import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

# Load saved model
model = joblib.load("car_price_model.pkl")

# Car brand options
brands = [
    "Audi", "BMW", "Chevrolet", "Daewoo", "Datsun", "Fiat",
    "Force", "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar",
    "Jeep", "Kia", "Land", "Mahindra", "Maruti",
    "Mercedes-Benz", "MG", "Mitsubishi", "Nissan",
    "Opel Corsa", "Renault", "Skoda", "Tata", "Toyota",
    "Volkswagen", "Volvo", "Other"
]

st.title("🚗 Used Car Price Prediction")
st.write("Enter the car details below.")

km_driven = st.number_input(
    "Kilometers Driven", min_value=0, value=50000
)

car_age = st.number_input(
    "Car Age (Years)", min_value=0, max_value=50, value=5
)

fuel = st.selectbox(
    "Fuel Type", ["Diesel", "Electric", "LPG", "Petrol", "CNG"]
)

seller_type = st.selectbox(
    "Seller Type", ["Individual", "Dealer", "Trustmark Dealer"]
)

transmission = st.selectbox(
    "Transmission", ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner", [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)

brand = st.selectbox("Car Brand", brands)

if st.button("Predict Selling Price"):

    # Create one row with all training columns
    input_data = pd.DataFrame(
        0, index=[0], columns=model.feature_names_in_
    )

    # Set numeric features
    input_data["km_driven"] = km_driven
    input_data["car_age"] = car_age

    # Set categorical features
    for col, value in [
        (f"fuel_{fuel}", 1),
        (f"seller_type_{seller_type}", 1),
        (f"transmission_{transmission}", 1),
        (f"owner_{owner}", 1),
        (f"brand_{brand}", 1)
    ]:
        if col in input_data.columns:
            input_data[col] = value

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Selling Price: ₹{prediction:,.0f}")
    st.caption(
        "This is an estimated price; actual market value may differ."
    )