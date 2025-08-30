import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]

ax.violinplot(all_data, orientation='horizontal')
plt.show()