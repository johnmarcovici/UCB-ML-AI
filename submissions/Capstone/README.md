# Capstone Project - Stock Market Analysis & Forecasting
This project analyzes stock-market data for the purposes of recommending one of the following actions per day, per stock analyzed:
- Buy
- Don't Buy

## Approach
The analysis writeup follows the CRISP-DM framework. The specific approach to answering the above questions is machine learning as applied to the stock market, AKA algorithmic trading.

## Data
Data sets were downloaded from [Yahoo Finance](https://finance.yahoo.com/) for the individual stocks, and for the S&P 500, from [Market Watch](https://www.marketwatch.com/investing/index/spx/download-data?startDate=4/8/2024&endDate=07/05/2024).

## What to Run
The writeup is [in this notebook](./stock_market_analysis_chipped.ipynb).

## Findings
2 types of models were considered:
- Decision trees and random forests
- Neural network based models

### Decision Trees and Random Forests
For the decision tree models, a classifier was attempted
- The target feature - buy or don't buy - was based on the difference in the stock price in the last 2 days of a training window
- Windows of 7 days were considered, giving 5 days to train on, and then the difference between day 7 and day 6 was calcuated: positive difference is labeled a buy
- For training, the stock data was divided in random chips of 7 days
- 

## Future Work