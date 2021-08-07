import pandas as pd
from bokeh.plotting import figure
from bokeh.io import export_svg


def inflation(df: pd.DataFrame):
    return df.pct_change() * 100


def readData(path: str):
    return pd.read_csv(path, skiprows=1, header=0, sep=';', decimal=',', index_col=0)


def plotInflation():
    # Subsection 'b' plot
    path: str = '../db/Table 1_3.csv'
    inf_df: pd.DataFrame = inflation(readData(path))
    plt = figure(plot_width=1920 // 3, plot_height=1080 // 3)
    plt.line(x=inf_df.index, y=inf_df['USA'], legend_label='USA', line_color='blue', line_width=5)
    plt.line(x=inf_df.index, y=inf_df['Canada'], legend_label='Canada', line_color='red')
    plt.line(x=inf_df.index, y=inf_df['Japan'], legend_label='Japan', line_color='green')
    plt.line(x=inf_df.index, y=inf_df['France'], legend_label='France', line_color='orange')
    plt.line(x=inf_df.index, y=inf_df['Germany'], legend_label='Germany', line_color='purple')
    plt.line(x=inf_df.index, y=inf_df['Italy'], legend_label='Italy', line_color='cyan')
    plt.line(x=inf_df.index, y=inf_df['UK'], legend_label='UK', line_color='black')
    export_svg(plt, filename='../img/img[1-2][1].svg')


if __name__ == '__main__':
    plotInflation()
