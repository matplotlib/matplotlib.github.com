fig, axs = plt.subplot_mosaic([['A', 'right'], ['B', 'right']],
                              figsize=(4, 3), layout='constrained')
for ax_name in axs:
    axs[ax_name].text(0.5, 0.5, ax_name, ha='center', va='center')