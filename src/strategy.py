import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def simulate_strategy(df, y_pred):
    """
    Simulates a basic trading strategy based on model predictions.
    If prediction == 1, go long for the day (buy & hold during that day).
    """
    returns = df['Daily Return'].iloc[-len(y_pred):].reset_index(drop=True)
    strategy_returns = returns * y_pred
    return strategy_returns


def plot_cumulative_returns(strategy_returns, benchmark_returns):
    """
    Plots cumulative returns for the strategy and benchmark (buy & hold).
    """
    cumulative_strategy = (1 + strategy_returns).cumprod()
    cumulative_benchmark = (1 + benchmark_returns).cumprod()

    plt.figure(figsize=(14, 6))
    cumulative_strategy.plot(label='Strategy')
    cumulative_benchmark.plot(label='Buy & Hold')
    plt.title('Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.grid(True)
    plt.legend()
    plt.show()