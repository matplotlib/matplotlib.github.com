import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots()
patches = [mpatches.Circle((0, 0.5), 0.1), mpatches.Rectangle((0.5, 0), 0.2, 0.3)]
pc = PatchCollection(patches, facecolor='blue', edgecolor='black', label='My patches')
ax.add_collection(pc)
ax.legend()  # Now displays the label "My patches"