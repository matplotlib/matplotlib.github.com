fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

cols = 10
rows = 4
data = (
np.reshape(np.arange(0, cols, 1), (1, -1)) ** 2
+ np.reshape(np.arange(0, rows), (-1, 1))
+ np.random.random((rows, cols))*5
)
x = range(data.shape[1])
ax1.stackplot(x, data, hatch="x")
ax2.stackplot(x, data, hatch=["//","\\","x","o"])

ax1.set_title("hatch='x'")
ax2.set_title("hatch=['//','\\\\','x','o']")

plt.show()