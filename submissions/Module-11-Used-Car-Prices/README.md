# Used Car Prices
This module analyzes used-car pricing data obtained from Craigslist vehicle sales. The original data set, which I think is [this one from Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data), was reduced for the students and provided as a csv file. 

The prompt was a hypothetical scenario where a used-car dealership wants to "fine tune their inventory", and to do so wants a model to predict a vehicle's eventual sales price. The specifics of the fine-tuning the client desires are left unstated and open to interpretation, perhaps to emulate the very realistic scenario where a client wants *something*, but doesn't know exactly what.

The prompt also required that the modeling is to be done according to the CRISP-DM framework, a standardized process for data mining.

What follows is the last step of the framework - the deployment of the model - to the client in the form of a report.

The modeling and analysis is done in [this notebook](./used_car_prices.ipynb).

## Introduction
A client set of used car dealerships has requested a model to predict the probable sale price of a car. To obtain such a model we started with a large, publicly available data set on used car-transactions. Each record in this data set includes a vehicle's make, model, year, mileage, quality, and sale price, a few examples of which are shown here:

|id        |region                 |price|year  |manufacturer|model                |condition|cylinders  |fuel  |odometer|title_status|transmission|VIN              |drive|size     |type  |paint_color|state|
|----------|-----------------------|-----|------|------------|---------------------|---------|-----------|------|--------|------------|------------|-----------------|-----|---------|------|-----------|-----|
|7316155043|fort wayne             |54900|2019.0|ram         |3500 4x4 cummins     |excellent|6 cylinders|diesel|55822.0 |clean       |automatic   |3C7WR9CL5KG517631|4wd  |full-size|pickup|black      |in   |
|7303413468|rochester              |9900 |2017.0|ford        |focus titanium       |excellent|4 cylinders|gas   |26850.0 |salvage     |automatic   |1FADP3J22HL281300|fwd  |compact  |sedan |black      |mn   |
|7315499219|brownsville            |12350|2007.0|gmc         |sierra sle 1500      |like new |8 cylinders|gas   |167000.0|clean       |automatic   |1GCECT24LKJH73951|rwd  |full-size|pickup|white      |tx   |

From this data set, we built several models and assessed their quality relative to an accuracy requirement. No requirement was provided so we asserted one - that the model should predict the price within **$3,000**, on average, of the correct sale price.

## Approach
The overall process was done according to the CRISP-DM framework, which we believe afforded two critical benefits. For us, the practicioner, the framework provided a guided development process, with steps and checklists along the way. For the client, the use of the framework meant we could describe up front how we planned to do the work, and then communicate our work along the way according to this structure. Given how complicated data mining can get, it should also comfort the client to know we are following a *process*.

## Results and Key Findings
The modeling thus far did not meet the derived requirement. The best performance seen thus far has been **$3,150**, so although we failed to meet the requirement, we got pretty close. The client can use the performance against this requirement to build in sufficient margin per transaction such that they obtain profitable sales.

The modeling showed that the 3 most important features in predicting price are the vehicle's year, odometer, and what type of fuel (gas, diesel, electric, etc...). Also important, but to a lesser extent, are the vehicle's type and manufacturer. If a dealer can only obtain just a few features per vehicle, these are the ones to prioritize.

The least important feature was paint color, among those tested. Some features were left out of the modeling entirely, including the VIN, region, and sales ID, which is of course specific to each transaction.

Two features that have obvious importance in the real world but showed up as unimportant, in terms of the model's coefficients, are title status and condition. The reason these appeared unimportant is because the data set is composed mostly of vehicles with clean title status and vehicles in excellent, good, or like new condition, rendering these features effectively constants.

## Next Steps and Recommendations
The next step is to go over these findings with the candidate dealers and understand the suitability of the requirement, and more importantly, the model's performance against it. It might be good enough as is, or it may need additional refinement, in terms of either the model's performance against the requirement, or the requirement itself.
