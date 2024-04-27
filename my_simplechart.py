import matplotlib.pyplot as plt

# Data to display on the plot
x = [3, 1, 3]
y = [3, 2, 1]

# Plot a simple line chart with elements of x as x-axis and y as y-axis
plt.plot(x, y)
plt.title("Line Chart")

# Adding legends
plt.legend(["Line"])

# Display the plot
plt.show()
