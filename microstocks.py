import yfinance as yf
import matplotlib.pyplot as plt

#Test with DEV branch. Making those changes.
#Adding more changes for the merge

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def plot_stock_data(stock_data):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot candlestick chart
    ax.plot(stock_data.index, stock_data['Close'], label='Closing Price', linewidth=0.5)

    # Plot 50-day and 200-day moving averages
    stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['200_MA'] = stock_data['Close'].rolling(window=200).mean()
    ax.plot(stock_data.index, stock_data['50_MA'], label='50-day MA', color='blue')
    ax.plot(stock_data.index, stock_data['200_MA'], label='200-day MA', color='red')

    # Highlight up and down days with green and red candles
    for i in range(len(stock_data)):
        if stock_data['Open'][i] < stock_data['Close'][i]:
            ax.plot(stock_data.index[i], stock_data['Open'][i], 'g_', markersize=10)
            ax.plot([stock_data.index[i], stock_data.index[i]], [stock_data['Open'][i], stock_data['Close'][i]], 'g-')
        elif stock_data['Open'][i] > stock_data['Close'][i]:
            ax.plot(stock_data.index[i], stock_data['Open'][i], 'r_', markersize=10)
            ax.plot([stock_data.index[i], stock_data.index[i]], [stock_data['Open'][i], stock_data['Close'][i]], 'r-')

    # Indicate crossover points
    crossover_points = stock_data[stock_data['50_MA'] > stock_data['200_MA']]
    ax.plot(crossover_points.index, crossover_points['Close'], '^', markersize=10, color='green', label='50-200 crossover')

    crossunder_points = stock_data[stock_data['50_MA'] < stock_data['200_MA']]
    ax.plot(crossunder_points.index, crossunder_points['Close'], 'v', markersize=10, color='red', label='50-200 crossunder')

    # Customize plot
    ax.set_title('Microsoft Stock Analysis')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    ticker = 'MSFT'
    start_date = '2012-01-01'
    end_date = '2022-01-01'

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    plot_stock_data(stock_data)
