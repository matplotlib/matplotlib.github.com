fig = plt.figure()
ax = fig.add_subplot(projection="polar")
ax.set_rlim(0, 1.2)

ax.axhline(1, c="C0", alpha=.5)
ax.axhspan(.8, .9, fc="C1", alpha=.5)
ax.axhspan(.6, .7, .8, .9, fc="C2", alpha=.5)