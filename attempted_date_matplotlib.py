import matplotlib.pyplot as plt
import csv
filename = '/data/weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)


dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%y-%m-%d')
    high = int(row[5])
    highs.append(high)
    dates.append(current_date)
    


fig,ax = plt.subplots()
ax.plot(dates,highs,c='blue',linewidth= 5)

plt.show()
