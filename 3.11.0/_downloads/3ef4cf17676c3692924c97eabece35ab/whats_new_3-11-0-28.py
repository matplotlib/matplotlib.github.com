fig = plt.figure()
ax = fig.add_subplot(projection="3d")

X = [i for i in range(10)]
Y = [i for i in range(10)]
Z = [i for i in range(10)]
S = [(i + 1) * 400 for i in range(10)]

ax.scatter(
    xs=X, ys=Y, zs=Z, s=S,
    depthshade=True,
    depthshade_minalpha=0.3,
)
ax.view_init(elev=10, azim=-150, roll=0)