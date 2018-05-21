import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import pickle

years = mdates.YearLocator()
months = mdates.MonthLocator()
yearsFmt = mdates.DateFormatter('%Y')

#with cbook.get_sample_data('goog.npy') as datafile:
    #datafile = pickle._dumps(np.unicode(df))
    #datafile = np.unicode(df)
#    r = np.load(datafile)['price_data'].view(np.recarray)
with np.load("C:\\Python35\\Lib\\site-packages\\matplotlib\\mpl-data\\sample_data\\goog.npy") as datafile:
    r = datafile['price_data'].view(np.recarray)

date = r.date.astype('O')

fig, ax = plt.subplots()
ax.plot(date, r.adj_close)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

datemin = datetime.date(date.min().year, 1, 1)
datemax = datetime.date(date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)

def price(x):
    return '$%1.2f' % x
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = price
ax.grid(True)

fig.autofmt_xdate()
plt.show()