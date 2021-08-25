import pandas as pd
from bokeh.plotting import figure
from bokeh.io import export_svg, output_file, show


def inflation(df: pd.DataFrame):
    return df.pct_change() * 100


def readData(path: str):
    return pd.read_csv(path, skiprows=1, header=0, sep=';', decimal=',', index_col=0)


def plotInflation():
    # Subsection 'b' plot
    path: str = '../db/Table 1_3.csv'
    inf_df: pd.DataFrame = inflation(readData(path))

    plt = figure(plot_width=1920 // 2, plot_height=1080 // 2)

    plt.line(x=inf_df.index, y=inf_df['USA'] - inf_df['USA'], legend_label='USA', line_color='blue', line_width=5)
    plt.line(x=inf_df.index, y=((inf_df['USA'] - inf_df['Canada']) / inf_df['Canada']) * 100, legend_label='Canada',
             line_color='red', line_width=2)
    plt.line(x=inf_df.index, y=((inf_df['USA'] - inf_df['Japan']) / inf_df['Japan']) * 100, legend_label='Japan',
             line_color='green', line_width=2)
    plt.line(x=inf_df.index, y=((inf_df['USA'] - inf_df['France']) / inf_df['France']) * 100, legend_label='France',
             line_color='orange', line_width=2)
    plt.line(x=inf_df.index, y=((inf_df['USA'] - inf_df['Germany']) / inf_df['Germany']) * 100, legend_label='Germany',
             line_color='purple', line_width=2)
    plt.line(x=inf_df.index, y=((inf_df['USA'] - inf_df['Italy']) / inf_df['Italy']) * 100, legend_label='Italy',
             line_color='cyan', line_width=2)
    plt.line(x=inf_df.index, y=((inf_df['USA'] - inf_df['UK']) / inf_df['UK']) * 100, legend_label='UK',
             line_color='black',
             line_width=2)
    export_svg(plt, filename='../img/img[1-2][1].svg')
    show(plt)


if __name__ == '__main__':
    plotInflation()
