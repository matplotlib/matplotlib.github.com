import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-7, 7, 140)
x = np.hstack([-25, x, 25])
fig, ax = plt.subplots()
ax.boxplot([x, x], notch=True, capwidths=[0.01, 0.2])
plt.show()