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
- Training windows of 7 consecutive days were randomly chosen from a list of 50 stocks and 90 days of history per stock
- Models were fit using both the stock price and its first derivative
- Total trading gains were calculated assuming a risk of $100 per trade, per day
- All models scored highly in training sets, and exhibited good accuracy - often 70% or higher, on the test sets
    - Howevever, due to a highly imbalanced class - 80% of samples were classified as do not buy, these relatively high test accuracies were not good enough to produce profitable gains over many days of trading

### Neural Network (NN) Models
A total of 3 neural-network models were considered, and the target feature was regression (time series regression) rather than the classifier models referenced above

#### Data Preparation
For the NN models, the data set used was the S&P 500 index from the last 6 years, approximately July 2018 to July 2024
- The data set was split into 80% training and 20% test
- The data was then arranged into overlaping windows of 6 days of training and 1 day as the target feature
- The data was log-transformed and scaled to a range of 0, 1 for presentation to the NN models

#### Basic NN
To form a baseline for comparison for the remaining NN models, a basic NN was developed with
- 1 fully connected hidden layer consisting of 8 neurons and relu activation
- 1 output layer with no activation

#### Simple RNN
A simple RNN was developed with
- 

#### LSTM

## Future Work