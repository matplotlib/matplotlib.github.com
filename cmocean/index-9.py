import cmocean
import matplotlib.pyplot as plt

cmap = cmocean.cm.oxy
fig, axes = plt.subplots(1, 2, figsize=(8,4))
A = np.random.randint(0, 101, (10,10))
mappable = axes[0].pcolormesh(A, vmin=0, vmax=100, cmap=cmap)
axes[0].set_title('Values go to super-saturated')
fig.colorbar(mappable, ax=axes[0])

newcmap = cmocean.tools.crop_by_percent(cmap, 20, which='max', N=None)
A[A>80] = 80
mappable = axes[1].pcolormesh(A, vmin=0, vmax=80, cmap=newcmap)
axes[1].set_title('Values are all\nbelow super-saturated')
fig.colorbar(mappable, ax=axes[1])