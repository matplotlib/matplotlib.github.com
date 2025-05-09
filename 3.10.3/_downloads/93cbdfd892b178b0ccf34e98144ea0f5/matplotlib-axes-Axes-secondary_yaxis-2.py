fig, ax = plt.subplots()
ax.plot(range(0, 5), range(-1, 4))

# Pass 'ax.transData' as a transform to place the axis
# relative to your data at x=3
secax = ax.secondary_yaxis(3, transform=ax.transData)