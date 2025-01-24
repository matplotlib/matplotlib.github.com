import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(-2, 2, 50)[np.newaxis, :]
y = np.linspace(-2, 2, 50)[:, np.newaxis]
im_0 = 1 * np.exp( - (x**2 + y**2 - x * y))
im_1 = 2 * np.exp( - (x**2 + y**2 + x * y))

colorizer = mpl.colorizer.Colorizer()
fig, axes = plt.subplots(1, 2, figsize=(6, 2))
cim_0 = axes[0].imshow(im_0, colorizer=colorizer)
fig.colorbar(cim_0)
cim_1 = axes[1].imshow(im_1, colorizer=colorizer)
fig.colorbar(cim_1)

colorizer.vmin = 0.5
colorizer.vmax = 2
colorizer.cmap = 'RdBu'