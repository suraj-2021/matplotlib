import matplotlib.pyplot as plt
from datetime import datetime
import csv

filename = "data/chandigarh_tempratures_2023.csv"  # Corrected file extension to .csv
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[3], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        # Append to the lists
        dates.append(date)
        highs.append(high)
        lows.append(low)

# Plotting the temperature graph
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5, label="Highs")  # Added label for highs
ax.plot(dates, lows, c='blue', alpha=0.5, label="Lows")  # Added label for lows
# Styling the curve
plt.title("Temperature Curve of Chandigarh 2023", fontsize=24)
plt.xlabel("Date")  # Added x-axis label
plt.ylabel("Temperature (°C)")  # Added y-axis label
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.legend()  # Added legend
plt.show()
