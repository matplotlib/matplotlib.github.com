import matplotlib as mpl

# Set visibility for major and minor gridlines
mpl.rcParams["axes.grid"] = True
mpl.rcParams["ytick.minor.visible"] = True
mpl.rcParams["xtick.minor.visible"] = True
mpl.rcParams["axes.grid.which"] = "both"

# Using grid.* to set both major and minor properties
mpl.rcParams["grid.color"] = "lightgrey"

# Overwrite some values for major and minor separately
mpl.rcParams["grid.major.linewidth"] = 1.2
mpl.rcParams["grid.minor.color"] = "tab:blue"
mpl.rcParams["grid.minor.linestyle"] = ":"

plt.plot([0, 1], [0, 1])