from matplotlib.collections import EllipseCollection

rng = np.random.default_rng(0)

widths = (2, )
heights = (3, )
angles = (45, )
offsets = rng.random((10, 2)) * 10

fig, ax = plt.subplots()

ec = EllipseCollection(
    widths=widths,
    heights=heights,
    angles=angles,
    offsets=offsets,
    units='x',
    offset_transform=ax.transData,
    )

ax.add_collection(ec)
ax.set_xlim(-2, 12)
ax.set_ylim(-2, 12)

new_widths = rng.random((10, 2)) * 2
new_heights = rng.random((10, 2)) * 3
new_angles = rng.random((10, 2)) * 180

ec.set(widths=new_widths, heights=new_heights, angles=new_angles)