import cmocean
import cmocean.cm as cmo
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 3))
ax = fig.add_subplot(1, 2, 1)
Z = np.random.randn(10,10)
ax.pcolormesh(Z, cmap=cmo.matter)

ax = fig.add_subplot(1, 2, 2)
lightcmap = cmocean.tools.lighten(cmo.matter, 0.5)
ax.pcolormesh(Z, cmap=lightcmap)
fig.tight_layout()