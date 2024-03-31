import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
cubic_numbers = [1,8,27,64,75]

fig,ax = plt.subplots()
plt.style.use("fivethirtyeight")
ax.plot(x_values,cubic_numbers,c = 'red', linewidth = 5)
ax.set_title("5 Cubic Numbers")
ax.set_xlabel("First Five Natural Number",fontsize=10)
ax.set_ylabel("First Five Cubic Numbers", fontsize = 10)
ax.tick_params(axis='both', which = 'major',labelsize = 10)

plt.show()
