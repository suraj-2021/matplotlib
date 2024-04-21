import plotly.graph_objects as go

# Create a scattergeo trace
trace = go.Scattergeo(
    lon=landslide_data['longitude'],
    lat=landslide_data['latitude'],
    mode='markers',
    marker=dict(
        size=10,
        color='red',
        opacity=0.7,
        symbol='circle'
    ),
    text=landslide_data['magnitude']
)

# Create a layout
layout = go.Layout(
    title='World Map of Landslides',
    geo=dict(
        showland=True,
        landcolor='lightgray',
        projection_type='natural earth'
    )
)

# Create the figure
fig = go.Figure(data=[trace], layout=layout)

# Show the plot
fig.show()
