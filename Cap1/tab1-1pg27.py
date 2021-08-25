import pandas as pd
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
data = pd.read_csv('../db/Table 1_1.csv', skiprows=7, header=1)
y90 = data.Y1
y91 = data.Y2
p90 = data.X1
p91 = data.X2
income90 = y90 * p90
income91 = y91 * p91
# plt.bar(data.STATE, y90 * p90, color="green")
# plt.bar(data.STATE, y91 * p91, color=(0.50, 0.30, 0.70, 1))
plt.barh(data.STATE, (income90 - income91) * 100 / income91, color=(0.50, 0.30, 0.70, 1), label="Percent Variance")
plt.hist((income90 - income91) * 100 / income91, color=(0.50, 0.30, 0.70, 0.3), label="Histogram",
         bins=int(math.sqrt(50)))

plt.title("Income Percent Variance (1990 - 1991)")
plt.xlabel("Percentage")
plt.ylabel("States")
plt.legend()
# plt.show()
plt.savefig('../img/img1.png', dpi=100, bbox_inches='tight')
