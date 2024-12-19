import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 3))
z = [[0, 1], [1, 2]]

ax1.contour(z, colors=('r', 0.4))
ax2.contour(z, colors=(0.1, 0.2, 0.5))

plt.show()