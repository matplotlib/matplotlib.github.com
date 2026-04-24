import matplotlib.pyplot as plt
import numpy as np

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2

fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, num_arrows=3)

plt.show()