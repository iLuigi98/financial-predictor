import numpy as np

def calculate_cumulative_return(returns):
    return (1 + returns).cumprod()

def calculate_annualized_return(returns, periods_per_year=252):
    cumulative = (1 + returns).prod()
    n_periods = len(returns)
    return cumulative ** (periods_per_year / n_periods) - 1

def calculate_annualized_volatility(returns, periods_per_year=252):
    return returns.std() * np.sqrt(periods_per_year)

def calculate_sharpe_ratio(returns, risk_free_rate=0.01, periods_per_year=252):
    ann_return = calculate_annualized_return(returns, periods_per_year)
    ann_vol = calculate_annualized_volatility(returns, periods_per_year)
    excess_return = ann_return - risk_free_rate
    return excess_return / ann_vol if ann_vol != 0 else np.nan

def calculate_max_drawdown(cumulative_returns):
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown.min()