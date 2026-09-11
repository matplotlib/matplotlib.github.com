fig = plt.figure(layout="constrained")
sfs = fig.subfigures(2)

ax0 = sfs[0].add_subplot()
ax0.plot([1, 2], label=r"$\rlap{\text{foo}}\phantom{\text{a longer label}}$")
sfs[0].legend(loc="outside right upper")

ax1 = sfs[1].add_subplot()
ax1.plot([1, 2], label="foo")
ax1.plot([2, 1], label="a longer label")
sfs[1].legend(loc="outside right upper")