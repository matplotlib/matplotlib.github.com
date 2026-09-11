x = np.linspace(0, 10)
y1 = x + np.sin(x)
y2 = x + np.cos(x)

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, facecolor=['tab:orange', 'tab:green'])