import requests

# Make a GET request to the Cat Fact API
response = requests.get("https://catfact.ninja/fact")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    cat_fact_data = response.json()  # Parse the response as JSON
    print("Cat Fact:", cat_fact_data["fact"])
else:
    print("Error fetching cat fact. Status code:", response.status_code)
