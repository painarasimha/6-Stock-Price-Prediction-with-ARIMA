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
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df['Date'], df['Close/Last'], label='Close Price')
    ax1.set_title('Stock Close Price Over Time')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Close Price')
    ax1.legend()
    figures.append(fig1)

    # 2. Volume Bar Chart
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.bar(df['Date'], df['Volume'], color='blue')
    ax2.set_title('Trading Volume Over Time')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Volume')
    figures.append(fig2)
    
    # 3. Moving Averages
    df['MA20'] = df['Close/Last'].rolling(window=20).mean()
    df['MA50'] = df['Close/Last'].rolling(window=50).mean()
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    ax3.plot(df['Date'], df['Close/Last'], label='Close Price')
    ax3.plot(df['Date'], df['MA20'], label='20-Day MA')
    ax3.plot(df['Date'], df['MA50'], label='50-Day MA')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Close Price')
    ax3.set_title('Stock Close Price and Moving Averages')
    ax3.legend()
    figures.append(fig3)

    # 4. Correlation Matrix
    corr = df[['Volume', 'Open', 'High', 'Low', 'Close/Last']].corr()
    fig4, ax4 = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax4)
    ax4.set_title('Correlation Heatmap')
    figures.append(fig4)
    
    # 5. Distribution of Daily Returns
    df['Daily Return'] = df['Close/Last'].pct_change()
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True, ax=ax5)
    ax5.set_title('Distribution of Daily Returns')
    ax5.set_xlabel('Daily Return')
    ax5.set_ylabel('Frequency')
    figures.append(fig5)
    
    # 6. Volatility Over Time
    df['Volatility'] = df['Close/Last'].rolling(window=20).std()
    fig6, ax6 = plt.subplots(figsize=(12, 6))
    ax6.plot(df['Date'], df['Volatility'], label='Volatility')
    ax6.set_xlabel('Date')
    ax6.set_ylabel('Volatility')
    ax6.set_title('Volatility Over Time')
    ax6.legend()
    figures.append(fig6)

    return figures
