import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import Image
img = Image.open('../_static/stinkbug.png')  # opens the file using PIL - it's not an array yet
rsize = img.resize((img.size[0]/10,img.size[1]/10))  # resize the image
rsizeArr = np.asarray(rsize)
lum_img = rsizeArr[:,:,0]
imgplot = plt.imshow(rsizeArr)