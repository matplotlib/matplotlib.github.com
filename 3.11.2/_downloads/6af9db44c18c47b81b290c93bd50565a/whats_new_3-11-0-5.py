np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)

ax1.set_title('Default violin plot')
ax1.set_ylabel('Observed values')
ax1.violinplot(data)

ax2.set_title('Set colors of violins')
ax2.set_ylabel('Observed values')
ax2.violinplot(
    data,
    facecolor=[('yellow', 0.3), ('blue', 0.3), ('red', 0.3), ('green', 0.3)],
    linecolor='black',
)