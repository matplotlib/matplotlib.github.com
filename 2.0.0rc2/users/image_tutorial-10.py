import matplotlib.pyplot as plt
from PIL import Image
img = Image.open('../_static/stinkbug.png')  # opens the file using Pillow - it's not an array yet
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img, interpolation="bicubic")