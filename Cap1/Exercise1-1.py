import pandas as pd
from bokeh.plotting import show
from bokeh.models import ColumnDataSource, DataTable, TableColumn

def inflation(df: pd.DataFrame):
    return df.pct_change() * 100


def readData(path: str):
    return pd.read_csv(path, skiprows=1, header=0, sep=';', decimal=',', index_col=0)


def showTable(df: pd.DataFrame):
    source = ColumnDataSource(df)
    columns = [TableColumn(field=col, title=col) for col in df.columns]
    dataTable = DataTable(source=source, columns=columns, index_position=0)
    show(dataTable)

def plotInflation():
    pass


def index_a():
    path: str = '../db/Table 1_3.csv'
    inf_df = inflation(readData(path))
    print(inf_df.to_markdown())

if __name__ == '__main__':
    path: str = '../db/Table 1_3.csv'
    inf_df = inflation(readData(path))
    # res_df = (df - df.iloc[5]) / df.iloc[5]
