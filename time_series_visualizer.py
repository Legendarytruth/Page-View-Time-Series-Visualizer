import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col=0,
    parse_dates=True)

#print(df)
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot figsize=(30, 10)
    fig, axes = plt.subplots(figsize=(3, 1))
    
    
    sns.lineplot(x = "date", y = "value", data = df).set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    df_bar["year"] = df.index.year
    df_bar["Months"] = df.index.month
    #print(df_bar)
    labels = ['January', 'February', 'March', 'April' , 'May' , 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot figsize=(15, 15)
    fig, axes = plt.subplots(figsize=(1, 1))

    sns.barplot(x = "year", y = "value", hue = "Months" ,data = df_bar).set(title="Average daily page views, by Month", xlabel="Years", ylabel="Average Page Views")
    plt.legend(labels=labels)
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    labels = ['Jan', 'Feb', 'Mar', 'Apr' , 'May' , 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn) figsize=(20,10)
    fig, axes = plt.subplots(1,2, figsize=(20,10))

    sns.boxplot(data=df_box, x='year', y='value', orient='v', ax=axes[0]).set(title='Year-wise Box Plot (Trend)',xlabel='Year', ylabel='Page Views')
    sns.boxplot(data=df_box, x='month', y='value', orient='v', order=labels, ax=axes[1]).set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
