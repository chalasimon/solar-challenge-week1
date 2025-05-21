# importing libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Solar Potential Dashboard")
st.write("This dashboard provides insights into solar potential data.")

# loading dataset
@st.cache
def load_data():
    benin_df = pd.read_csv('../data/benin-malanville_clean.csv')
    sierra_leone_df = pd.read_csv('../data/sierraleone-bumbuna_clean.csv')
    togo_df = pd.read_csv('../data/togo-dapaong_clean.csv')
    return pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)
data = load_data()


