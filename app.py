"""
World GDP Choropleth Map Visualization

Visualizes the GDP of countries using a Plotly choropleth map.
Author: Ganesh
"""

import plotly.graph_objects as go
import pandas as pd

def load_data(url):
    """Load GDP data from a CSV URL."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def create_choropleth(df):
    """Create a choropleth map from the dataframe."""
    fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorscale = 'Blues',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'GDP Billions USD',
    ))

    # Update the layout for better visualization
    fig.update_layout(
        title_text='World GDP Visualization (2014)',
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular'
        ),
        annotations = [dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">CIA World Factbook</a>',
            showarrow = False
        )]
    )
    return fig

def main():
    DATA_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv'
    df = load_data(DATA_URL)
    if df is not None:
        fig = create_choropleth(df)
        fig.show()
    else:
        print("Failed to load data. Please check the data source.")

if __name__ == "__main__":
    main()