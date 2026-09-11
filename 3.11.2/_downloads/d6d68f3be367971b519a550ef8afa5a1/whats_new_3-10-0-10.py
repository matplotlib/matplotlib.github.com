import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Note that when a line has one vertex outside the view limits, the entire
# line is hidden. The same is true for 3D patches (not shown).
# In this example, data where x < 0 or z > 0.5 is clipped.
ax.plot_wireframe(X, Y, Z, color='C0')
ax.plot_wireframe(X, Y, Z, color='C1', axlim_clip=True)
ax.set(xlim=(0, 10), ylim=(-5, 5), zlim=(-1, 0.5))
ax.legend(['axlim_clip=False (default)', 'axlim_clip=True'])