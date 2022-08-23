from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 3, subplot_kw={'projection': '3d'},
                        constrained_layout=True)
X, Y, Z = axes3d.get_test_data(0.05)
focal_lengths = [0.25, 1, 4]
for ax, fl in zip(axs, focal_lengths):
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    ax.set_proj_type('persp', focal_length=fl)
    ax.set_title(f"focal_length = {fl}")
plt.tight_layout()
plt.show()