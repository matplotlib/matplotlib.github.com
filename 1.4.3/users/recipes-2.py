import matplotlib.cbook as cbook
datafile = cbook.get_sample_data('goog.npy')
r = np.load(datafile).view(np.recarray)
plt.figure()
plt.plot(r.date, r.close)
plt.title('Default date handling can cause overlapping labels')