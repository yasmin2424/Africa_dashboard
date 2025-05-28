# unemployment.py
import pandas as pd
import plotly.express as px
import os

def process_data(path):
    # Load unemployment data from the assets folder
    employ_df = pd.read_csv(path, skiprows=3)
    countries_of_interest = ["Ethiopia", "Ghana", "Kenya", "Nigeria", "Sub-Saharan Africa", "Uganda", "World"]

    columns_of_interest = ['Country Name'] + [str(year) for year in range(2011, 2025)]
    df_selected = employ_df[columns_of_interest]

    df_filtered = df_selected[df_selected['Country Name'].isin(countries_of_interest)]
    df_filtered


    
    return df_filtered

def get_unemployment_chart():

    df = process_data("assets/Unemployment.csv")
    df_long = df.melt(id_vars='Country Name', var_name='Year', value_name='Value')
    df_long['Year'] = df_long['Year'].astype(int)

    # Create the plot
    fig = px.line(df_long, x='Year', y='Value', color='Country Name',
                title='Unemployment Trends (2011–2024)',
                labels={'Value': 'Value', 'Year': 'Year'})
    return fig
