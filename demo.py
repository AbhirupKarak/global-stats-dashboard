import streamlit as st
import pandas as pd
# from datetime import date
# from dateutil.relativedelta import relativedelta
# import datetime
# st.title("hello chai app")
# st.subheader("brewed with streamlit")
# st.text("wlcm")
# st.write("Choose your fav lang")

# chai = st.selectbox("your fav lang", ['python','c++', 'java', 'rust'])

# st.write(chai)

# st.success("slctd")

# st.title("Chai Maker App")
# if st.button("Make Chai"):
#     st.success("Your Chai is being brewed.")

# add_masala = st.checkbox("Add Masala")
# if add_masala:
#     st.write("Masala added to your chai.")

# tea_type = st.radio("Pick your Chai base : ",['Milk', 'Water', 'Honey'])
# st.write(f"Selected base is {tea_type}.")

# flavor = st.selectbox("Choose flavor : ",['Adrak', 'Kesar', 'Lemon'])
# st.write(f"Selected flavor is {flavor}.")

# sugar = st.slider("Sugar Level (in tsp)", 0, 5, 1)

# st.number_input("How many cups? ", min_value=1, max_value=10)

# name = st.text_input("Enter your name: ")

# st.title("Age Calculator")

# dob = st.date_input("Enter your date of birth", min_value=datetime.date(1900,1,1))

# today = date.today()
# age = relativedelta(today, dob)
# st.write(f"Your age is {age.years} years, {age.months} months and {age.days} days old.")

# st.title("Chai taste poll")

# col1, col2 = st.columns(2)

# with col1:
#     st.header("Masala Chai")
#     vote1 = st.button("Vote Masala Chai")
#     st.image("https://images.pexels.com/photos/17546504/pexels-photo-17546504.jpeg", width=100)

# with col2:
#     st.header("Adrak Chai")
#     vote2 = st.button("Vote Adrak Chai")

# if vote1:
#     st.success("Thanks for voting Masala Chai")
# elif vote2:
#     st.success("Thanks for voting Adrak Chai")

# name = st.sidebar.text_input("Enter your name")
# tea = st.sidebar.selectbox("Choose your chai", ['masala', 'kesar', 'adrak'])

# st.write(f"Hey {name} your {tea} chai is getting ready")

# with st.expander("Show Chai making instr"):
#     st.write(""" 
#             1. Boil Water with tea leaves
#             2. Add Milk and spices
#             3. serve
# """)
    
# st.markdown("#Welcome to Chai App")
# st.markdown("> BlockQuote")

# st.title("Chai Sales Dashboard")
# file = st.file_uploader("Upload your csv file", type=['csv'])

# if file:
#     df = pd.read_csv(file)
#     st.subheader("Data preview")
#     st.dataframe(df)

#     st.subheader("Summary stats")
#     st.write(df.describe())

#     cities = df["City"].unique()
#     selected_city = st.selectbox("Filter by cities", cities)
#     filtered_data = df[df["City"] == selected_city]
#     st.dataframe(filtered_data)

import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter the amount : ", min_value=0.0, step=0.01)
tar_curr = st.selectbox("Convert to", ['USD', 'GBP', 'JPY', 'EUR'])
if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][tar_curr]
        converted_value = rate*amount
        st.success(f"{amount} INR = {converted_value} {tar_curr}")
    else:
        st.error("Failed to fetch conversion rate")