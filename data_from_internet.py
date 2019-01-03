import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(
        stock_price_url).read().decode('utf-8')

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    # %Y = full year 2019
    # %y = partial year 19
    # %m =
    date, openp, highp, lowp, closep, adjusted_closep, volume = np.loadtxt(
        stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})

    plt.plot_date(date, closep)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stuck Data')
    plt.legend()
    plt.show()


graph_data('TSLA')
