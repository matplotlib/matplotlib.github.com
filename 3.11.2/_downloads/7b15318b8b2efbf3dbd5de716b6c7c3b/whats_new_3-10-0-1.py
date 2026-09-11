import numpy as np
import matplotlib.pyplot as plt

vals = np.linspace(-5, 5, 100)
x, y = np.meshgrid(vals, vals)
img = np.sin(x*y)

_, ax = plt.subplots(1, 3)
ax[0].imshow(img, cmap="berlin")
ax[1].imshow(img, cmap="managua")
ax[2].imshow(img, cmap="vanimo")