import matplotlib.pyplot as plt

squares = [1,4,8,16,20,24]

fig,ax = plt.subplots()

ax.plot(squares, linewidth = 3)
ax.set_title("Square Number", fontsize = 20)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize = 12)

#set size of tick labes
ax.tick_params(axis='both', labelsize=14)
plt.show()
