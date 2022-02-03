import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('../_static/stinkbug.png')
lum_img = img[:, :, 0]
plt.imshow(lum_img)