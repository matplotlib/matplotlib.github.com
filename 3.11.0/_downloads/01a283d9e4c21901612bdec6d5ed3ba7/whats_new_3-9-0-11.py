from matplotlib import animation
from matplotlib.patches import Arrow

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

a = Arrow(2, 0, 0, 10)
ax.add_patch(a)


# code for modifying the arrow
def update(i):
    a.set_data(x=.5, dx=i, dy=6, width=2)


ani = animation.FuncAnimation(fig, update, frames=15, interval=90, blit=False)

plt.show()