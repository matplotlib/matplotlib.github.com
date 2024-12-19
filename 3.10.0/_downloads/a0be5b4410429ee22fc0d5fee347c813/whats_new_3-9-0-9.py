fig, axs = plt.subplots(1, 2, subplot_kw={'projection': '3d'})

plt.rcParams['axes3d.automargin'] = True
axs[0].set(xlim=(0, 1), ylim=(0, 1), zlim=(0, 1), title='Old Behavior')

plt.rcParams['axes3d.automargin'] = False  # the default in 3.9.0
axs[1].set(xlim=(0, 1), ylim=(0, 1), zlim=(0, 1), title='New Behavior')