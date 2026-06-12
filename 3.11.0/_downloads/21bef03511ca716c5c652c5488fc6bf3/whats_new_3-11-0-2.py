fig, ax = plt.subplots()
ax.axhline(0, color='tab:red')
ax.broken_barh([(0, 10)], (0, 2))  # Default is 'bottom'.
ax.axhline(10, color='tab:red')
ax.broken_barh([(0, 10)], (10, 2), align='center')
ax.axhline(20, color='tab:red')
ax.broken_barh([(0, 10)], (20, 2), align='top')