x = np.linspace(1, 10, 10)
y1, y2 = x, -x
fig = plt.figure(constrained_layout=True)
subfigs = fig.subfigures(nrows=1, ncols=2)
for subfig in subfigs:
    axarr = subfig.subplots(2, 1)
    for ax in axarr.flatten():
        (l1,) = ax.plot(x, y1, label="line1")
        (l2,) = ax.plot(x, y2, label="line2")
subfigs[0].set_zorder(6)
l = fig.legend(handles=[l1, l2], loc="upper center", ncol=2)