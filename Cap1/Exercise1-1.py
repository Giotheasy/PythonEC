import pandas as pd
from bokeh.plotting import show, figure
from bokeh.models import ColumnDataSource, DataTable, TableColumn
from bokeh.io import export_svg


def inflation(df: pd.DataFrame):
    return df.pct_change() * 100


def readData(path: str):
    return pd.read_csv(path, skiprows=1, header=0, sep=';', decimal=',', index_col=0)


def showTable(df: pd.DataFrame):
    source = ColumnDataSource(df)
    columns = [TableColumn(field=col, title=col) for col in df.columns]
    dataTable = DataTable(source=source, columns=columns, index_position=0)
    show(dataTable)


def drawTable():
    # Subsection 'a' table
    path: str = '../db/Table 1_3.csv'
    inf_df = inflation(readData(path))
    print(inf_df.to_markdown())
    print(inf_df.describe().to_markdown())


def plotInflation():
    # Subsection 'b' plot
    path: str = '../db/Table 1_3.csv'
    inf_df: pd.DataFrame = inflation(readData(path))
    plt = figure(plot_width=1920 // 3, plot_height=1080 // 3)
    plt.line(x=inf_df.index, y=inf_df['USA'], legend_label='USA', line_color='blue', line_width=2)
    plt.line(x=inf_df.index, y=inf_df['Canada'], legend_label='Canada', line_color='red', line_width=2)
    plt.line(x=inf_df.index, y=inf_df['Japan'], legend_label='Japan', line_color='green', line_width=2)
    plt.line(x=inf_df.index, y=inf_df['France'], legend_label='France', line_color='orange', line_width=2)
    plt.line(x=inf_df.index, y=inf_df['Germany'], legend_label='Germany', line_color='purple', line_width=2)
    plt.line(x=inf_df.index, y=inf_df['Italy'], legend_label='Italy', line_color='cyan', line_width=2)
    plt.line(x=inf_df.index, y=inf_df['UK'], legend_label='UK', line_color='black', line_width=2)
    export_svg(plt, filename='../img/img[1-1][1].svg')

def drawStats():
    # Subsection 'd' table
    path: str = '../db/Table 1_3.csv'
    inf_df = inflation(readData(path))
    print(inf_df.describe().to_markdown())


if __name__ == '__main__':
    drawStats()
    plotInflation()