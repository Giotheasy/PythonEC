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
s = input("Insert the exercise code [Ex.: 1.1a]: ")
if s == "1.1a":
    plt.plot(data.Year, data.InfCa, marker='*', label='Canada')
    plt.plot(data.Year, data.InfFr, marker='v', label='France')
    plt.plot(data.Year, data.InfGe, marker='D', label='Germany')
    plt.plot(data.Year, data.InfIt, marker='d', label='Italy')
    plt.plot(data.Year, data.InfJa, marker='P', label='Japan')
    plt.plot(data.Year, data.InfUK, marker='8', label='United Kingdom')
    plt.plot(data.Year, data.InfUS, marker='<', label='United States')
elif s == '1.2a':
    # plt.plot(data.Year, data.InfUS, marker='<', label='United States', linewidth=4)
    print("Select the required graph (US vs ...)\n"
          "1. Canada\n"
          "2. France\n"
          "3. Germany\n"
          "4. Italy\n"
          "5. Japan\n"
          "6. United Kingdom"
          )
    gp = int(input())
    if gp == 1:
        # plt.plot('Year', 'InfCa', data=data, marker='*', label='Canada')
        plt.plot(data.Year, data.InfCa / data.InfUS, marker='*', label='Canada')
    elif gp == 2:
        plt.plot(data.Year, data.InfFr / data.InfUS, marker='v', label='France')
    elif gp == 3:
        plt.plot(data.Year, data.InfGe / data.InfUS, marker='D', label='Germany')
    elif gp == 4:
        plt.plot(data.Year, data.InfIt / data.InfUS, marker='d', label='Italy')
    elif gp == 5:
        plt.plot(data.Year, data.InfJa / data.InfUS, marker='P', label='Japan')
    elif gp == 6:
        plt.plot(data.Year, data.InfUK / data.InfUS, marker='8', label='United Kingdom')
    else:
        print("Invalid command")
else:
    print("Command not found")
plt.title("Inflation rate between 1973 - 1997", size=20)
plt.legend()
plt.show()
