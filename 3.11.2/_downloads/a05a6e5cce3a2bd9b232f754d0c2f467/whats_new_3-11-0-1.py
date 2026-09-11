categories = ['A', 'B']
datasets = {
    'dataset 0': [1, 11],
    'dataset 1': [3, 13],
    'dataset 2': [5, 15],
}

fig, ax = plt.subplots()
ax.grouped_bar(datasets, tick_labels=categories)
ax.legend()