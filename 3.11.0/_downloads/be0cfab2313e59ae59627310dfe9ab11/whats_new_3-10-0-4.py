import matplotlib.pyplot as plt

fig = plt.figure()
subfigs = fig.subfigures(3, 3)
x = np.linspace(0, 10, 100)

for i, sf in enumerate(fig.subfigs):
    ax = sf.subplots()
    ax.plot(x, np.sin(x + i), label=f'Subfigure {i+1}')
    sf.suptitle(f'Subfigure {i+1}')
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()