# importing libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Solar Potential Dashboard")
st.write("This dashboard provides insights into solar potential data.")

# loading dataset

def load_data():
    benin_df = pd.read_csv('./data/benin-malanville_clean.csv')
    sierra_leone_df = pd.read_csv('./data/sierraleone-bumbuna_clean.csv')
    togo_df = pd.read_csv('./data/togo-dapaong_clean.csv')
    benin_df['country'] = 'Benin'
    sierra_leone_df['country'] = 'Sierra Leone'
    togo_df['country'] = 'Togo'
    combined_df = pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)
    return combined_df
df = load_data()
#widget to select country
country = st.multiselect(
    "Select Country",
    options=df['country'].unique(),
    default=df['country'].unique()
)

# filtering data based on selected country
filtered_data = df[df['country'].isin(country)]




