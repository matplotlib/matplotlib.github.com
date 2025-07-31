import matplotlib.pyplot as plt
import numpy as np
np.random.seed(19680801)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(9, 9))

data1 = np.random.poisson(5, 1000)
data2 = np.random.poisson(7, 1000)
data3 = np.random.poisson(10, 1000)

labels = ["Data 1", "Data 2", "Data 3"]

ax1.hist([data1, data2, data3], bins=range(17), histtype="step", stacked=True,
         edgecolor=["red", "green", "blue"], linewidth=[1, 2, 3])
ax1.set_title("Different linewidths")
ax1.legend(labels)

ax2.hist([data1, data2, data3], bins=range(17), histtype="barstacked",
         hatch=["/", ".", "*"])
ax2.set_title("Different hatch patterns")
ax2.legend(labels)

ax3.hist([data1, data2, data3], bins=range(17), histtype="bar", fill=False,
         edgecolor=["red", "green", "blue"], linestyle=["--", "-.", ":"])
ax3.set_title("Different linestyles")
ax3.legend(labels)

ax4.hist([data1, data2, data3], bins=range(17), histtype="barstacked",
         facecolor=["red", "green", "blue"])
ax4.set_title("Different facecolors")
ax4.legend(labels)

plt.show()