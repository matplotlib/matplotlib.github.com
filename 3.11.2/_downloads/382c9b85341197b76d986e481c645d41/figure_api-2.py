fig = plt.figure(layout='constrained', figsize=(4, 2.5), facecolor='lightgoldenrodyellow')

# Make two subfigures, left ones more narrow than right ones:
sfigs = fig.subfigures(1, 2, width_ratios=[0.8, 1])
sfigs[0].set_facecolor('khaki')
sfigs[1].set_facecolor('lightsalmon')

# Add subplots to left subfigure:
lax = sfigs[0].subplots(2, 1)
sfigs[0].suptitle('Left subfigure')

# Add subplots to right subfigure:
rax = sfigs[1].subplots(1, 2)
sfigs[1].suptitle('Right subfigure')

# suptitle for the main figure:
fig.suptitle('Figure')