np.random.seed(19680801)

fig, ax = plt.subplots()

x = [29, 36, 41, 25, 32, 70, 62, 58, 66, 80, 58, 68, 62, 37, 48]
y = [82, 76, 48, 53, 62, 70, 84, 68, 55, 75, 29, 25, 12, 17, 20]
colors = ['tab:blue'] * 5 + ['tab:orange'] * 5 + ['tab:green'] * 5

ax.scatter(
    x,
    y,
    s=800,
    hatch="xxxx",
    hatchcolor=colors,
    facecolor="none",
    edgecolor="black",
)