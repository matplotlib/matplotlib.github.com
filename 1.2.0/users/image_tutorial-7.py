import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
fig = plt.figure()
a=fig.add_subplot(1,2,1)
img = mpimg.imread('../_static/stinkbug.png')
lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
a.set_title('Before')
plt.colorbar(ticks=[0.1,0.3,0.5,0.7], orientation ='horizontal')
a=fig.add_subplot(1,2,2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0,0.7)
a.set_title('After')
plt.colorbar(ticks=[0.1,0.3,0.5,0.7], orientation='horizontal')