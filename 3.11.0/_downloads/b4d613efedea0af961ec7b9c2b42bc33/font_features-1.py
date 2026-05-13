fig = plt.figure(figsize=(7, 3))

fig.text(0.5, 0.85, 'Ligatures', fontsize=40, horizontalalignment='center')

# Default has Standard Ligatures (liga).
fig.text(0, 0.6, 'Default: fi ffi fl st', fontsize=40)

# Disable Standard Ligatures with -liga.
fig.text(0, 0.35, 'Disabled: fi ffi fl st', fontsize=40,
         fontfeatures=['-liga'])

# Enable Discretionary Ligatures with dlig.
fig.text(0, 0.1, 'Discretionary: fi ffi fl st', fontsize=40,
         fontfeatures=['dlig'])