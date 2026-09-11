fig, ax = plt.subplots()
ax.plot(range(0, 5), range(-1, 4))

# Pass 'ax.transData' as a transform to place the axis
# relative to your data at y=0
secax = ax.secondary_xaxis(0, transform=ax.transData)