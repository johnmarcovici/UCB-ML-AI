# Introduction

A client set of used car dealerships has requested a model to predict the probable sale price of a car. Their stated purpose for obtaining such a model was to *fine tune their inventory* which we interpret to mean make more efficient transactions per vehicle, ultimately leading to a more profitable enterprise.

To obtain such a model we started with a large, publicly available [data set](./data/vehicles_no_nulls_shuffled_top_100.csv) from Kaggle on used car transactions that stretches back decades. Each record in this data set includes a vehicle's make, model, year, mileage, quality, and sale price. From this data set, we built several models and assessed their quality relative to a derived requirement.

# Approach
The overall process was done according to the CRISP-DM framework, which we believe afforded two critical benefits. For us, the practicioner, the framework provided a guided development process, which steps and checklists along the way, while being general enough that we could adapt as needed. For the client, the use of the framework meant we could describe up front how we planned to do the work, and then communicate our work along the way according to this structure. Given how complicated data mining can get, it should also comfort the client to know we are following a *process*.

# Results and Key Findings
To help guide the modeling process, we derived a requirement for the model to predict within **$3,000**, on average, of the correct sale price. The modeling thus far did not meet this requirement. The best performance seen thus far has been **$3,150**, so although we failed to meet the requirement, we got pretty close. The client can use this requirement to build in sufficient margin per transaction such that they obtain profitable sales.

# Next Steps and Recommendations
