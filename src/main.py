from src.features import preprocess_features
from src.model import prepare_data, train_random_forest, evaluate_model
from src.strategy import simulate_strategy, plot_cumulative_returns
from src.backtest import calculate_sharpe_ratio, calculate_max_drawdown
from src.utils import get_feature_columns


def main():
    print("\n🔄 Loading and processing data...")
    df = preprocess_features("data/sp500.csv")

    print("\n📊 Preparing features and training/test sets...")
    features = get_feature_columns()
    X_train, X_test, y_train, y_test, _ = prepare_data(df, features)

    print("\n🌲 Training Random Forest model...")
    model = train_random_forest(X_train, y_train)

    print("\n🧪 Evaluating model...")
    y_pred = evaluate_model(model, X_test, y_test)

    print("\n💰 Simulating strategy returns...")
    strategy_returns = simulate_strategy(df, y_pred)
    benchmark_returns = df['Daily Return'].iloc[-len(y_pred):].reset_index(drop=True)

    print("\n📈 Plotting performance...")
    plot_cumulative_returns(strategy_returns, benchmark_returns)

    print("\n📉 Calculating backtest metrics...")
    sharpe = calculate_sharpe_ratio(strategy_returns)
    drawdown = calculate_max_drawdown((1 + strategy_returns).cumprod())
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Max Drawdown: {drawdown:.2%}")


if __name__ == "__main__":
    main()