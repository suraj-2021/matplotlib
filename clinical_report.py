import pandas as pd
import plotly.express as px

# Load the blood report data
df = pd.read_csv('blood_report.csv')

# Create a bar chart
fig = px.bar(df, x='Parameter', y='Value', title='Blood Report')

# Add a line to represent the normal range
fig.add_shape(
    type='line',
    x0=0,
    x1=len(df['Parameter']),
    y0=df['Normal_Range'].mean(),
    y1=df['Normal_Range'].mean(),
    line=dict(color='Red'),
)

# Show the plot
fig.show()
