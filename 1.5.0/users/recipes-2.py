import matplotlib.cbook as cbook
datafile = cbook.get_sample_data('goog.npy')
try:
    # Python3 cannot load python2 .npy files with datetime(object) arrays
    # unless the encoding is set to bytes. Hovever this option was
    # not added until numpy 1.10 so this example will only work with
    # python 2 or with numpy 1.10 and later.
    r = np.load(datafile, encoding='bytes').view(np.recarray)
except TypeError:
    # Old Numpy
    r = np.load(datafile).view(np.recarray)
plt.figure()
plt.plot(r.date, r.close)
plt.title('Default date handling can cause overlapping labels')