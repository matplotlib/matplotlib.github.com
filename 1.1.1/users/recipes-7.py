np.random.seed(1234)
fig, ax = plt.subplots(1)
ax.plot(np.random.randn(300), 'o-', label='normal distribution')
ax.plot(np.random.rand(300), 's-', label='uniform distribution')
ax.set_ylim(-3, 3)
leg = ax.legend(loc='best', fancybox=True)
leg.get_frame().set_alpha(0.5)

ax.set_title('fancy, transparent legends')