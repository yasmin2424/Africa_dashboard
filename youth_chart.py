# youth_chart.py

import pandas as pd
import plotly.express as px
import os

def get_youth_population_chart():
    # Load youth population data from the assets folder
    data_path = os.path.join("assets", "youth_population_africa.csv")
    youth_df = pd.read_csv(data_path)

    # Sort and take top 10
    top10_df = youth_df.sort_values("Youth_Population_15_24_Millions", ascending=False).head(10)

    # Create bar chart
    fig = px.bar(
        top10_df,
        x="Country",
        y="Youth_Population_15_24_Millions",
        title="Top 10 African Countries by Youth Population (Ages 15–24)",
        labels={"Youth_Population_15_24_Millions": "Youth Population (Millions)"},
        template="plotly_white"
    )
    return fig
