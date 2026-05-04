import streamlit as st
import seaborn as sb
import pandas as pd

df = pd.read_csv(r"C:\Games\CODE\python\project\birth_rate.csv", skiprows=3)

df_long = df.melt(
    id_vars = ['Country Name', 'Country Code', 'Indicator Name', "Indicator Code"],
    var_name = 'year',
    value_name="birth_rate"
)

df_long = df_long[df_long["year"] != "Unnamed: 70"]
df_long["year"] = df_long["year"].astype(int)
df_long = df_long.dropna(subset=["birth_rate"])

print(df_long.head())
print(df_long.shape)