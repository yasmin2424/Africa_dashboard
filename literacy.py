# unemployment.py
import pandas as pd
import plotly.express as px
import os

def process_data(path):
    # Load unemployment data from the assets folder
    employ_df = pd.read_csv(path, skiprows=3)
    countries_of_interest = ["Sub-Saharan Africa", "World"]

    columns_of_interest = ['Country Name'] + [str(year) for year in range(2011, 2024)]
    df_selected = employ_df[columns_of_interest]

    df_filtered = df_selected[df_selected['Country Name'].isin(countries_of_interest)]
    df_filtered


    
    return df_filtered

def get_literacy_chart():

    df = process_data("assets/Literacy_levels.csv")
    df_long = df.melt(id_vars='Country Name', var_name='Year', value_name='Value')
    df_long['Year'] = df_long['Year'].astype(int)

    # Create the plot
    fig = px.line(df_long, x='Year', y='Value', color='Country Name',
                title='Literacy Trend  (2011–2023)',
                labels={'Value': 'Value', 'Year': 'Year'})
    return fig
