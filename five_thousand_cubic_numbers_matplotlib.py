import matplotlib.pyplot as plt
x_values = range(0,5001)
y_values = [x**3 for x in x_values]

fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,linewidth=5)

ax.set_title("Cube of First 5000 Numbers", fontsize=20)
ax.set_xlabel("5000 Natural Numbers", fontsize=13)
ax.set_ylabel("Cube of 5000 Natural Numbers", fontsize=13)
ax.tick_params(axis = "both", which="major", labelsize=11)

plt.show()
