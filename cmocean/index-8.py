import cmocean
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)
Z = np.random.randn(10,10)
ax.pcolormesh(Z, cmap='cmo.amp')