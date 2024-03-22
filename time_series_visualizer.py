import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col=['date'])

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df['value'], c='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_monthly = df_bar.resample('M').mean()
    df_monthly['year'] = df_monthly.index.year
    df_monthly['month'] = df_monthly.index.month_name()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.barplot(data=df_monthly, x='year', y='value', hue='month', palette='tab10', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title="Months")





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=ax[1])
    ax[0].set_xlabel("Year")
    ax[1].set_xlabel("Month")
    ax[0].set_ylabel("Page Views")
    ax[1].set_ylabel("Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
