import cmocean
import matplotlib.pyplot as plt

cmap = cmocean.cm.tarn
fig, axes = plt.subplots(1, 2, figsize=(8,4))
A = np.random.randint(-5, 6, (10,10))
mappable = axes[0].pcolormesh(A, cmap=cmap)
axes[0].set_title('Full diverging colormap')
fig.colorbar(mappable, ax=axes[0])

newcmap = cmocean.tools.crop_by_percent(cmap, 30, which='both', N=None)
mappable = axes[1].pcolormesh(A, cmap=newcmap)
axes[1].set_title('Same colormap,\n30% removed from each end')
fig.colorbar(mappable, ax=axes[1])