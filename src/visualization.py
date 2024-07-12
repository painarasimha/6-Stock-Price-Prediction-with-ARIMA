# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Visualizations

def visualize(data):
    df = pd.read_csv(data)

    # Replacing '$' with ''.
    df['Close/Last'] = df['Close/Last'].str.replace('$', '', regex=False).astype('float64')
    df['Open'] = df['Open'].str.replace('$', '', regex=False).astype('float64')
    df['High'] = df['High'].str.replace('$', '', regex=False).astype('float64')
    df['Low'] = df['Low'].str.replace('$', '', regex=False).astype('float64')

    figures = []

    # Visualizations of the df

    # 1. Line Plot of stock prices over time
    fig1 = plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close/Last'], label='Close Price')
    plt.title('Stock Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.savefig('results/line_plot_stock_prices.png')
    figures.append(fig1)
    plt.close(fig1)

    # 2. Volume Bar Chart
    fig2 = plt.figure(figsize=(12,6))
    plt.bar(df['Date'], df['Volume'], color='blue')
    plt.title('Trading Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.savefig('results/volume_bar_chart.png')
    figures.append(fig2)
    plt.close(fig2)
    
    # 3. Moving Averages
    df['MA20'] = df['Close/Last'].rolling(window=20).mean()
    df['MA50'] = df['Close/Last'].rolling(window=50).mean()
    fig3 = plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close/Last'], label='Close Price')
    plt.plot(df['Date'], df['MA20'], label='20-Day MA')
    plt.plot(df['Date'], df['MA50'], label='50-Day MA')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Close Price and Moving Averages')
    plt.legend()
    plt.savefig('results/moving_averages.png')
    figures.append(fig3)
    plt.close(fig3)

    # 4. Correlation Matrix
    corr = df[['Volume', 'Open', 'High', 'Low', 'Close/Last']].corr()

    fig4 = plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('results/Correlation_matrix.png')
    figures.append(fig4)
    plt.close(fig4)
    
    # 5. Distribution of Daily Returns
    df['Daily Return'] = df['Close/Last'].pct_change()
    fig5 = plt.figure(figsize=(10,6))
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True)
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.savefig('results/daily_returns_dist.png')
    figures.append(fig5)
    plt.close(fig5)
    
    # 6. Volatility Over Time
    df['Volatility'] = df['Close/Last'].rolling(window=20).std()
    fig6 = plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Volatility'], label='Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.title('Volatility Over Time')
    plt.legend()
    plt.savefig('results/volatility.png')
    figures.append(fig6)
    plt.close(fig6)

    return figures
