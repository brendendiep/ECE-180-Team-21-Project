import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from dateutil.parser import parse
import pandas as pd
import numpy as np

with open('BTC_USD(coinmarketcap).json', 'rb') as fp:
	data = json.load(fp)

print "Column Names\n", "=>",
column_names = data.keys()
for c in column_names:
	print c,
print '\n',data['description']
prices = data['data']
high_price = [p[2] for p in prices]
low_price = [p[3] for p in prices]
Date = [p[0] for p in prices]
for i in range(len(Date)):
	Date[i] = datetime.strptime(Date[i], '%b %d %Y')
plt.style.use('ggplot')
plt.figure(figsize=(10,4))
plt.plot_date(x=Date, y=high_price, fmt="r-",linewidth=0.5, label='high')
plt.plot_date(x=Date, y=low_price, fmt="b-",linewidth=0.5, label='low')
plt.grid(True)
plt.title("BTC prices")
plt.xlabel("date")
plt.ylabel("prices($)")
plt.legend()
plt.savefig("BitCoin.png", dpi=720)
plt.show()