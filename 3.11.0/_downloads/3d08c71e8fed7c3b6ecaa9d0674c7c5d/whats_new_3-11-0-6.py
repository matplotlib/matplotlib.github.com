data = [36, 24, 8, 12]
labels = ['spam', 'eggs', 'bacon', 'sausage']

fig, ax = plt.subplots()
pie = ax.pie(data)

ax.pie_label(pie, labels, distance=1.1)
ax.pie_label(pie, '{frac:.1%}', distance=0.7)
ax.pie_label(pie, '{absval:d}', distance=0.4)