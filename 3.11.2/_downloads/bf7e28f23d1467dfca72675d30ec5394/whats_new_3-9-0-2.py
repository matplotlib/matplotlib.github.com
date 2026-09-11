fig, ax = plt.subplots()

data_A = np.random.random((100, 3))
data_B = np.random.random((100, 3)) + 0.2
pos = np.arange(3)

ax.boxplot(data_A, positions=pos - 0.2, patch_artist=True, label='Box A',
           boxprops={'facecolor': 'steelblue'})
ax.boxplot(data_B, positions=pos + 0.2, patch_artist=True, label='Box B',
           boxprops={'facecolor': 'lightblue'})

ax.legend()