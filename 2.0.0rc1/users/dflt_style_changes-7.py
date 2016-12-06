data = np.random.lognormal(size=(37, 4))
fig, (old, new) = plt.subplots(ncols=2, sharey=True)
with plt.style.context('default'):
    new.boxplot(data, labels=['A', 'B', 'C', 'D'])
    new.set_title('New boxplots')

with plt.style.context('classic'):
    old.boxplot(data, labels=['A', 'B', 'C', 'D'])
    old.set_title('Old boxplots')

new.set_ylim(bottom=0)