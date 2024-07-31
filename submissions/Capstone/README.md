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
- The data was then arranged into overlapping windows of 6 days of training and 1 day as the target feature
- The data was log-transformed and scaled to a range of 0, 1 for presentation to the NN models

#### Basic NN
To form a baseline for comparison for the remaining NN models, a basic NN was developed with
- 1 fully connected hidden layer consisting of 8 neurons and relu activation
- 1 output layer with no activation

#### Simple RNN
A simple RNN was developed with
- a hidden RNN layer with 16 units and tanh activation
- 1 output layer with no activation

#### LSTM
Lastly, an LSTM was developed with
- a hidden layer with 8 units and exponential activation
- 1 output layer with no activation

Each of these NN models were assessed for average error during the training and test periods, with the average error defined as the average of the percentage of error comparing the regression value to its target. The LSTM was the strongest performer of these three models, with an average error in test of -0.3%, compared to almost 3% for the RNN
- The error is defined as y_true - y_estimated, so a negative error means the estimate is higher than the true value, on average

Additionally, confusion matrices were computed for each model
- Although the model did not output a classification, the regression value was used to decide to buy or not to buy
    - Positive expected gains are interpreted as a buy signal

Lastly, the effective trading gain per model was calculated
- The effective gain is defined as the difference between the active trading gain and the passively invested gain
    - The active gain is what arises from using the above rule to trade (if gain is predicted then buy) with respect to a fixed investment per trade of $100
    - The passively invested gain is computed the return from $100 if invested on day 1 of the test period and sold on the final day
- All 3 NN models exhibited negative effective trading gain
    - While both the basic NN and RNN exhibited positive active gain, the passive gain was larger, so the effective gain was negative
    - Meanwhile, the LSTM model exhibited both a negative active gain and a negative passive gain
- So despite the complexity of these models, they were on average worse than simply passively investing

## Future Work