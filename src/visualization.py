import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize(data):
    df = pd.read_csv(data)

    # Function to clean and convert to float
    def clean_and_convert_to_float(column):
        df[column] = df[column].str.replace('[\$,]', '', regex=True).astype('float64')

    # Clean and convert columns
    clean_and_convert_to_float('Close/Last')
    clean_and_convert_to_float('Open')
    clean_and_convert_to_float('High')
    clean_and_convert_to_float('Low')
    clean_and_convert_to_float('Volume')

    # Visualizations of the df

    # 1. Line Plot of stock prices over time
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close/Last'], label='Close Price')
    plt.title('Stock Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    line_plot_path = 'results/line_plot_stock_prices.png'
    plt.savefig(line_plot_path)
    plt.close()

    # 2. Volume Bar Chart
    plt.figure(figsize=(12,6))
    plt.bar(df['Date'], df['Volume'], color='blue')
    plt.title('Trading Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    volume_chart_path = 'results/volume_bar_chart.png'
    plt.savefig(volume_chart_path)
    plt.close()
    
    # 3. Moving Averages
    df['MA20'] = df['Close/Last'].rolling(window=20).mean()
    df['MA50'] = df['Close/Last'].rolling(window=50).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close/Last'], label='Close Price')
    plt.plot(df['Date'], df['MA20'], label='20-Day MA')
    plt.plot(df['Date'], df['MA50'], label='50-Day MA')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Close Price and Moving Averages')
    plt.legend()
    moving_averages_path = 'results/moving_averages.png'
    plt.savefig(moving_averages_path)
    plt.close()

    # 4. Correlation Matrix
    corr = df[['Volume', 'Open', 'High', 'Low', 'Close/Last']].corr()

    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    correlation_matrix_path = 'results/Correlation_matrix.png'
    plt.savefig(correlation_matrix_path)
    plt.close()
    
    # 5. Distribution of Daily Returns
    df['Daily Return'] = df['Close/Last'].pct_change()
    plt.figure(figsize=(10,6))
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True)
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    daily_returns_path = 'results/daily_returns_dist.png'
    plt.savefig(daily_returns_path)
    plt.close()
    
    # 6. Volatility Over Time
    df['Volatility'] = df['Close/Last'].rolling(window=20).std()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Volatility'], label='Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.title('Volatility Over Time')
    plt.legend()
    volatility_path = 'results/volatility.png'
    plt.savefig(volatility_path)
    plt.close()

    return {
        'line_plot': line_plot_path,
        'volume_chart': volume_chart_path,
        'moving_averages': moving_averages_path,
        'correlation_matrix': correlation_matrix_path,
        'daily_returns': daily_returns_path,
        'volatility': volatility_path
    }
