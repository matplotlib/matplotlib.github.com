z = np.random.randn(10)

p1a, = plt.plot(z, "ro", ms=10, mfc="r", mew=2, mec="r") # red filled circle
p1b, = plt.plot(z[:5], "w+", ms=10, mec="w", mew=2) # white cross

plt.legend([p1a, (p1a, p1b)], ["Attr A", "Attr A+B"])