import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
data = pd.read_csv("../db/Table 1_2.csv", header=0)
data['InfCa'] = data.Canada.pct_change() * 100
data['InfFr'] = data.France.pct_change() * 100
data['InfGe'] = data.Germany.pct_change() * 100
data['InfIt'] = data.Italy.pct_change() * 100
data['InfJa'] = data.Japan.pct_change() * 100
data['InfUK'] = data.UK.pct_change() * 100
data['InfUS'] = data.US.pct_change() * 100
inf = data.pct_change() * 100
# plt.plot(data.Year, data.InfCa)
# plt.plot(data.Year, data.InfFr)
plt.plot(data.Year, data.InfCa, marker='*', label='Canada')
plt.plot(data.Year, data.InfFr, marker='v', label='France')
plt.plot(data.Year, data.InfGe, marker='D', label='Germany')
plt.plot(data.Year, data.InfIt, marker='d', label='Italy')
plt.plot(data.Year, data.InfJa, marker='P', label='Japan')
plt.plot(data.Year, data.InfUK, marker='8', label='United Kingdom')
plt.plot(data.Year, data.InfUS, marker='<', label='United States')
plt.legend()
plt.show()
