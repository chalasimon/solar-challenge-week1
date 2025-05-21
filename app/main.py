# importing libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.plots import plot_boxplot # user defined library 

#loading the dataset
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


# Set  page configuration
st.set_page_config(
    page_title="Solar Potential Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)
#sidebar
st.sidebar.header("Solar Potential Dashboard")
st.sidebar.button("Home", key="home")
# Correct implementation of About button
about_clicked = st.sidebar.button("About")
if about_clicked:
    st.sidebar.markdown("""
    **About This Dashboard**
    
    This interactive dashboard provides insights into solar potential across multiple countries. 
    Explore solar irradiance data through:
    
    - Interactive visualizations (boxplots, scatter plots, histograms)
    - Comparative statistics by country
    - Top performance rankings
    
    **Data Metrics Included:**
    - Global Horizontal Irradiance (GHI)
    - Direct Normal Irradiance (DNI)
    - Diffuse Horizontal Irradiance (DHI)
    
    *Developed for MoonLight Energy Solutions*
    Chala Simon @ Kifiya AIM
    """)

# home page header
st.title("Solar Potential Dashboard")
st.write("This dashboard provides insights into solar potential data.")

col1, col2 = st.columns(2)

with col1:
    #widget to select country
    country = st.multiselect(
        "Select Country",
        options=df['country'].unique(),
        default=df['country'].unique()
    )
    metric = st.selectbox(
        'Select Metric',
        ['GHI', 'DNI', 'DHI']
    )

    # filtering data based on selected country
    filtered_data = df[df['country'].isin(country)]

    # plot filtered data 

    st.subheader(f'Boxplot of {metric} by Country')
    st.pyplot(plot_boxplot(filtered_data, metric))

with col2:
    show_table = st.checkbox("Show Top Regions Table", value=True)
    st.subheader('Summary Statistics:')
    if show_table:
        # Calculate rankings
        rankings = (filtered_data.groupby('country')[metric]
                    .agg(['mean', 'median', 'std'])
                    .sort_values('mean', ascending=False)
                    .reset_index())
        rankings.columns = ['Country', 'Mean', 'Median', 'Standard Deviation/ Variability']
        rankings['Mean'] = rankings['Mean'].round(2)
        rankings['Median'] = rankings['Median'].round(2)
        rankings['Standard Deviation/ Variability'] = rankings['Standard Deviation/ Variability'].round(2)
        
        # Display with style
        st.dataframe(
            rankings.style
            .highlight_max(subset=['Mean', 'Median'], color='lightgreen')
            .highlight_min(subset=['Standard Deviation/ Variability'], color='peachpuff'),
            use_container_width=True
        )
    else:
        st.write(filtered_data.groupby('country')[metric].agg(['mean', 'median','std']).reset_index())
# Additional visualizations expander
with st.expander("Advanced Visualizations"):
    tab1, tab2 = st.tabs(["Scatter Plot", "Histogram"])
    
    with tab1:
        st.subheader(f"{metric} vs. Temperature")
        fig, ax = plt.subplots()
        sns.scatterplot(
            data=filtered_data,
            x='Tamb',
            y=metric,
            hue='country',
            palette='viridis',
            alpha=0.6
        )
        st.pyplot(fig)
    
    with tab2:
        st.subheader(f"{metric} Distribution")
        fig, ax = plt.subplots()
        sns.histplot(
            data=filtered_data,
            x=metric,
            hue='country',
            element='step',
            kde=True,
            palette='viridis'
        )
        st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("**MoonLight Energy Solutions** - Solar Potential Analysis")