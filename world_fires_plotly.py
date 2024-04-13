import pandas as pd
import plotly.express as px

# Load the data from a CSV file
df = pd.read_csv('world_fire_data.csv')

# Create a scatter plot on a world map
fig = px.scatter_geo(df,
                     lat='Latitude',
                     lon='Longitude',
                     color='Intensity',
                     title='World Fire Data',
                     projection='natural earth')

# Show the plot
fig.show()
