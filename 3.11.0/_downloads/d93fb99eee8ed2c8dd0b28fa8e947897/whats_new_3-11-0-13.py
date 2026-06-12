plt.style.use('petroff6')
x = range(5)
for i in range(6):
    plt.plot(x, [v*(i+1) for v in x], label=f'line {i}')
plt.legend()