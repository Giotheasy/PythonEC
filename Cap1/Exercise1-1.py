import pandas as pd

data = pd.read_csv('../db/Table 1_3.csv', skiprows=1, header=0, sep=';')
print(data)
