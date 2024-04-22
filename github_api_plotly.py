import plotly.express as px
import requests

# Define the GitHub API endpoint
github_api_url = "https://api.github.com/repos/plotly/plotly.py"

# Make a GET request to the GitHub API
response = requests.get(github_api_url)

# Extract the number of stars and forks from the response
stars = response.json()["stargazers_count"]
forks = response.json()["forks_count"]

# Create a bar chart using Plotly Express
fig = px.bar(x=["Stars", "Forks"], y=[stars, forks], labels={"x": "Metric", "y": "Count"})

# Show the chart
fig.show()
