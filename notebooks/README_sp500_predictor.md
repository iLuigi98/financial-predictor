# 🧠 S&P 500 Market Predictor

A machine learning pipeline for predicting the daily directional movement of the S&P 500 index. This project is the first in a broader financial data science series aimed at showcasing applied ML, data engineering, and strategy simulation skills in real-world market contexts.

---

## 📈 Project Overview

This project uses historical S&P 500 OHLCV data to:
- Perform feature engineering using technical indicators
- Label market direction as UP or DOWN
- Train and evaluate multiple classification models (Logistic Regression, Random Forest, etc.)
- Simulate trading strategies based on model predictions
- Backtest the effectiveness of rule-based strategies

---

## 🔍 Key Features

- **Data Fetching**: Pulls historical S&P 500 data from Yahoo Finance with configurable start/end dates.
- **Feature Engineering**: Calculates common technical indicators (RSI, MACD, Bollinger Bands, etc.) for enhanced signal quality.
- **Model Evaluation**: Tests and compares classification models using precision, recall, F1-score, and confusion matrices.
- **Trading Strategy**: Implements simple buy/sell logic based on predictions with configurable thresholds.
- **Modular Codebase**: Python files are organized into modules (e.g., `features.py`, `strategy.py`, `backtest.py`) for scalability and reuse.
- **Notebook Walkthrough**: A detailed notebook explains each step of the pipeline and evaluates model performance critically.
- **Blog-Ready**: All work is structured for easy translation into blog content (e.g., Medium or personal site).

---

## 🧪 Technologies Used

- Python 3.11
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`
- `yfinance`
- `ta` (technical analysis library)
- `Docker` (planned)
- Jupyter Notebooks

---

## 📁 Project Structure

```
sp500-predictor/
│
├── data/                  # Raw and processed CSV data
├── notebooks/
│   ├── 01_eda.ipynb               # Exploratory analysis
│   ├── 04_modular_pipeline.ipynb # Pipeline using .py files
│
├── src/
│   ├── fetch_data.py
│   ├── features.py
│   ├── model.py
│   ├── strategy.py
│   ├── backtest.py
│   └── utils.py
│
├── app/
│   └── app.py               # (Reserved for potential web interface)
├── tests/
│   └── test_model.py        # Basic unit tests
│
├── requirements.txt
├── Dockerfile               # (To be finalized)
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/iLuigi98/sp500-predictor.git
cd sp500-predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Fetch fresh S&P 500 data
```bash
python src/fetch_data.py
```

### 4. Run the notebook
Open `01_sp500_predictor_detailed_walkthrough_v2.ipynb` or `04_modular_pipeline.ipynb` in Jupyter Notebook or JupyterLab.

---

## 📌 Future Improvements

- Add XGBoost and LightGBM with hyperparameter tuning
- Add rolling window validation and time-based cross-validation
- Experiment with macroeconomic indicators (e.g., CPI, unemployment rate)
- Build a simple front-end using Streamlit
- Explore live market predictions using WebSockets or Alpaca API

---

## 🧭 Project Series Roadmap

This is the first in a series of financial ML projects. Future topics include:
- Company fundamentals modeling (balance sheet, income, cash flow)
- NLP on earnings calls and news sentiment
- Risk modeling and volatility prediction
- A final real-time system for market decision making

---

## 👤 Author

**Luigi Cheng**  
Data Science Master's Student @ UC San Diego  
[GitHub](https://github.com/iLuigi98) | [Portfolio](https://luigidata.com) *(in progress)*

---

## 📝 License

MIT License. See `LICENSE` file for details.
