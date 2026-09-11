colors = plt.colormaps['okabe_ito'].colors
x = range(5)
for i, c in enumerate(colors):
    plt.plot(x, [v*(i+1) for v in x], color=c, label=f'line {i}')
plt.legend()