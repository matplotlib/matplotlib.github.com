fig, axs = plt.subplots(1, 2, layout='constrained')

axs[0].plot(np.arange(0, 1e6, 1000))
axs[0].set_title('Title 0')
axs[0].set_xlabel('XLabel 0')

axs[1].plot(np.arange(1, 0, -0.1) * 2000, np.arange(1, 0, -0.1))
axs[1].set_title('Title 1')
axs[1].set_xlabel('XLabel 1')
axs[1].xaxis.tick_top()
axs[1].tick_params(axis='x', rotation=55)

fig.align_labels()
fig.align_titles()