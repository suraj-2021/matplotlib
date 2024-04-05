# Rolling two dice
from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        
    def roll(self):
        return randint(1, self.num_sides)

# Create two instances of the Die class
die1 = Die()
die2 = Die()

# Calculate the maximum possible sum of the two dice rolls
max_sum = die1.num_sides + die2.num_sides

# Simulate rolling the dice 50001 times
results = [die1.roll() + die2.roll() for _ in range(50001)]

# Count the frequencies of each sum
frequencies = [results.count(value) for value in range(2, max_sum + 1)]

# Define x-axis values
x_values = list(range(2, max_sum + 1))

# Create a bar chart
data = [Bar(x=x_values, y=frequencies)]

# Configure the layout
my_layout = Layout(
    title="Rolling Two Dice for 50001 Times",
    xaxis={"title": "Total Value"},
    yaxis={"title": "Frequencies"}
)

# Generate the plot and save it to an HTML file
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")
