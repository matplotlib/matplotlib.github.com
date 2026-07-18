plt.style.use('petroff8')
x = range(5)
for i in range(8):
    plt.plot(x, [v*(i+1) for v in x], label=f'line {i}')
plt.legend()