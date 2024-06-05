# Comparison of Classifiers
This module compares 4 common classifiers for binary classification
- KNN
- Decision Trees
- Logistic Regression
- Support Vector Machines

on a sample data set provided. The data set is from a direct-marketing campaign carried out on behalf of a bank, with the objective to get customers to sign up for a long-term bank deposit. The target feature - yes or no - indicated whether or not a customer that received one or more phone calls from a bank representative signed up for the deposit. The stated purpose of the study that led to the data collection was to be able to continue to carry out direct marking campaigns but require fewer contacts per customer, while maintaining the same rate of subscriptin (saying yes) to the offered product.

The modeling and analysis is done in [this notebook](./practical_application_3.ipynb).

## Overview
The analysis begins by establishing a baseline model, which is given by the majority class (no, with 88% saying no). Next, a series of classifiers is developed, first non-optimized, then optimized, at each point comparing the performance.

### Modeling Approach
Next, a logistic regression is performed, using all default parameters. The logistic regression achieves just slightly higher performance than the trivial (baseline) model.

### Comparing Non-Optimized Classifiers
The performance from the logistic regression is then compared to the same obtained by 3 additional classifiers - KNN, Decision Trees, and Support Vector Machines. The results from these classifiers, as well as the time to fit and score the models, is collected in a dataframe for ease of comparison.

### Optiziming the Classifiers
Lastly, these same 4 classifiers are subject to a hyperparameter search using grid search, over a range of specified hyperparameter values. Again the performance and time to fit and score are collected.


## Findings

