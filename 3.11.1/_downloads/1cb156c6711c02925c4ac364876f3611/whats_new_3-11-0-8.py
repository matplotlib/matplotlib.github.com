from matplotlib.patches import Rectangle

fig, ax = plt.subplots()
rect = Rectangle((0.1, 0.1), 0.6, 0.6, fill=False,
                  edgecolor='orange', edgegapcolor='blue',
                  linestyle='--', linewidth=3)
ax.add_patch(rect)