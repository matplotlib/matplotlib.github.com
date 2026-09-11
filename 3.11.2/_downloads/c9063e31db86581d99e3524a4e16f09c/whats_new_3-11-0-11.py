fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5), layout='constrained')

pos = range(5)
labels = ['label'] * 5
ax1.set_xticks(pos, labels, rotation=-45, rotation_mode='xtick')
ax1.set_yticks(pos, labels, rotation=45, rotation_mode='ytick')
ax2.xaxis.tick_top()
ax2.set_xticks(pos, labels, rotation=-45, rotation_mode='xtick')
ax2.yaxis.tick_right()
ax2.set_yticks(pos, labels, rotation=45, rotation_mode='ytick')