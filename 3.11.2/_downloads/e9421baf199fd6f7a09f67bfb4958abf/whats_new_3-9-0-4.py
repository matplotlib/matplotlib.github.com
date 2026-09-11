# Fake data with reproducible random state.
np.random.seed(19680801)
data = np.random.normal(0, 8, size=100)

fig, ax = plt.subplots()

ax.violinplot(data, [0], showmeans=True, showextrema=True)
ax.violinplot(data, [1], showmeans=True, showextrema=True, side='low')
ax.violinplot(data, [2], showmeans=True, showextrema=True, side='high')

ax.set_title('Violin Sides Example')
ax.set_xticks([0, 1, 2], ['Default', 'side="low"', 'side="high"'])
ax.set_yticklabels([])