import matplotlib.pyplot as plt
import numpy as np

# Generate a range of values from 0 to 2*pi (360 degrees)
x = np.linspace(0, 2 * np.pi, 100)

# Calculate the sine of each value
y = np.sin(x)

# Create the plot
plt.plot(x, y)


plt.title('Sine Wave')
plt.xlabel('Angle [radians]')
plt.ylabel('sin(x)')


plt.grid(True)

# Display the plot
plt.show()
