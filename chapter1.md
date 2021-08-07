## Chapter 1

***

### Exercise 1.1

Table 1.3 gives data on the Consumer Price Index (CPI) for seven industrialized countries with 1982-1984 = 100 as the
base of the index.

```python
import pandas as pd


def inflation(df: pd.DataFrame):
    return df.pct_change() * 100


def readData(path: str):
    return pd.read_csv(path, skiprows=1, header=0, sep=';', decimal=',', index_col=0)


if __name__ == '__main__':
    path: str = '../db/Table 1_3.csv'
    inf_df = inflation(readData(path))
    print(inf_df.to_markdown())
```

a. From the given data, compute the inflation rate for each country

### Inflation (Percentage)

|      |       USA |     Canada |       Japan |     France |     Germany |     Italy |        UK |
|-----:|----------:|-----------:|------------:|-----------:|------------:|----------:|----------:|
| 1980 | nan       | nan        | nan         | nan        | nan         | nan       | nan       |
| 1981 |  10.3155  |  12.4836   |   4.84048   |  13.278    |   6.34371   |  19.3038  |  11.9745  |
| 1982 |   6.16062 |  10.8645   |   2.93809   |  11.9658   |   5.31453   |  16.313   |   8.53242 |
| 1983 |   3.21244 |   5.79557  |   1.73293   |   9.48746  |   3.29557   |  14.9373  |   4.61216 |
| 1984 |   4.31727 |   4.28287  |   2.30461   |   7.66932  |   2.39282   |  10.6151  |   5.01002 |
| 1985 |   3.56112 |   4.10697  |   2.05681   |   5.82794  |   2.04479   |   8.60987 |   6.01145 |
| 1986 |   1.85874 |   4.12844  |   0.671785  |   2.53497  |  -0.0954198 |   6.11065 |   3.42034 |
| 1987 |   3.64964 |   4.31718  |   0         |   3.23956  |   0.191022  |   4.59144 |   4.17755 |
| 1988 |   4.13732 |   4.05405  |   0.667302  |   2.72502  |   1.3346    |   4.98512 |   4.92899 |
| 1989 |   4.81826 |   4.9513   |   2.27273   |   3.45659  |   2.72813   |   6.59107 |   7.72293 |
| 1990 |   5.40323 |   4.79505  |   3.14815   |   3.3411   |   2.74725   |   6.11702 |   9.53437 |
| 1991 |   4.20811 |   5.60886  |   3.2316    |   3.15789  |   3.65419   |   6.39098 |   5.87045 |
| 1992 |   3.01028 |   1.53739  |   1.73913   |   2.40525  |   4.9871    |   5.30035 |   3.69662 |
| 1993 |   2.99359 |   1.7894   |   1.28205   |   2.13523  |   4.5045    |   4.25056 |   1.59803 |
| 1994 |   2.56055 |   0.20284  |   0.675105  |   1.60279  |   2.74295   |   3.91631 |   2.48034 |
| 1995 |   2.83401 |   2.15924  |  -0.0838223 |   1.78326  |   1.83066   |   5.36913 |   3.36482 |
| 1996 |   2.95276 |   1.5852   |   0.0838926 |   2.02156  |   1.49813   |   3.87065 |   2.45574 |
| 1997 |   2.29446 |   1.62549  |   1.84409   |   1.1889   |   1.69742   |   1.74528 |   3.12152 |
| 1998 |   1.55763 |   0.959693 |   0.576132  |   0.652742 |   0.943396  |   3.15253 |   3.45946 |
| 1999 |   2.20859 |   1.71103  |  -0.327332  |   0.518807 |   0.647017  |   1.66292 |   1.51515 |
| 2000 |   3.36134 |   2.74143  |  -0.656814  |   1.67742  |   1.42857   |   2.51989 |   2.98507 |
| 2001 |   2.84553 |   2.547    |  -0.743802  |   1.64975  |   1.97183   |   2.75981 |   1.74913 |
| 2002 |   1.58103 |   2.24719  |  -0.915903  |   1.93508  |   1.31215   |   2.51783 |   1.66994 |
| 2003 |   2.27904 |   2.77617  |  -0.252101  |   2.08206  |   1.09066   |   2.66066 |   2.89855 |
| 2004 |   2.66304 |   1.85706  |   0         |   2.15957  |   1.68577   |   2.19298 |   3.00469 |
| 2005 |   3.38804 |   2.1547   |  -0.336984  |   1.70288  |   1.92308   |   1.95084 |   2.82589 |

b. Plot the inflation rate for each country against the time (i.e., use the horizontal axis for time and the vertical
axis for the inflation rate)
![alt_text](img/img%5B1-1%5D%5B1%5D.svg "Inflation Plot")

c. What broad conclusions can you draw about the inflation experience in the seven countries?

d. Which country's inflation rate seems to be the most variable? Can you offer any explanation?

En lo siguiente se mostrara como se muestran las muestras



